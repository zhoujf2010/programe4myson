using Fleck;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.IO.Ports;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace scratch_link
{
    internal class HC06Session : Session
    {
        internal HC06Session(IWebSocketConnection webSocket) : base(webSocket)
        {
        }

        static SerialPort sp = null; //串口对象

        protected override async Task DidReceiveCall(string method, JObject parameters,
          Func<JToken, JsonRpcException, Task> completion)
        {
            switch (method)
            {
                case "connect":
                    await completion(await Connect(parameters), null);
                    break;
                case "disconnect":
                    await completion(await DisConnect(parameters), null);
                    break;
                case "send":
                    await completion(await SendMessage(parameters), null);
                    break; ;
                case "read":
                    await completion(await ReadMessage(parameters), null);
                    break;
                default:
                    throw JsonRpcException.MethodNotFound(method);
            }
        }

        private JObject lastparameters = null;


        private async Task<JToken> Connect(JObject parameters)
        {
            var port = parameters["port"]?.ToObject<string>();
            var baudrate = parameters["baudrate"]?.ToObject<int>();
            lastparameters = parameters;
            try
            {
                if (sp == null)
                {
                    sp = new SerialPort();
                    sp.PortName = port;
                    sp.BaudRate = (int)baudrate;
                    sp.DataReceived += Sp_DataReceived;
                    sp.ErrorReceived += Sp_ErrorReceived;
                    sp.PinChanged += Sp_PinChanged;
                    sp.Open();
                }
                dt = 0xff;

                if (!sp.CtsHolding)
                {//设备断开，则重新连接后发消息
                    sp.Close();
                    sp = null;
                    return await Connect(lastparameters);
                }

                //发送测试
                byte[] bts = new byte[1];
                bts[0] = 0;
                sp.Write(bts, 0, bts.Length);
                int p = 0;
                while (true)
                {
                    byte ss = getData();
                    if (ss != 0xff)
                        break;
                    Thread.Sleep(10);
                    p++;
                    if (p > 500)//连接失败.5秒
                    {
                        return new JObject
                        {
                            new JProperty("result", "Error"),
                            new JProperty("msg", "连接设备失败")
                        };

                    }
                }

                var peripheralInfo = new JObject
                {
                    new JProperty("result", "OK")
                };

                return peripheralInfo;
            }
            catch (Exception e)
            {
                var peripheralInfo = new JObject
                {
                    new JProperty("result", "Error"),
                    new JProperty("msg", e.Message)
                };
                sp = null;
                return peripheralInfo;
            }
        }

        private void Sp_PinChanged(object sender, SerialPinChangedEventArgs e)
        {
        }

        private void Sp_ErrorReceived(object sender, SerialErrorReceivedEventArgs e)
        {
        }

        private async Task<JToken> DisConnect(JObject parameters)
        {
            if (sp != null)
            {
                sp.Close();
                sp = null;
            }
            return null;
        }


        private async Task<JToken> SendMessage(JObject parameters)
        {
            var str = parameters["msg"]?.ToObject<string>();
            byte[] bts = new byte[1];// Encoding.UTF8.GetBytes(str);
            bts[0] = (byte)int.Parse(str);
            sp.Write(bts, 0, bts.Length);

            return null;
        }

        private async Task<JToken> ReadMessage(JObject parameters)
        {
            if (!sp.CtsHolding)
            {
                return new JObject
                {
                    new JProperty("result", "Error"),
                    new JProperty("msg", "设备断开")
                };

            }
            byte ss = getData();
            var peripheralInfo = new JObject
                {
                    new JProperty("result", "OK"),
                    new JProperty("msg", ss.ToString())
                };

            return peripheralInfo;
        }



        private void Sp_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            Byte[] readBytes = new Byte[sp.BytesToRead];
            int p = sp.Read(readBytes, 0, readBytes.Length);
            lock (this)
            {
                foreach (byte bt in readBytes)
                {
                    dt = bt;
                }
            }

            if (readBytes.Length == 0)
                Console.WriteLine("===>空");
            else
            {
                string ss = "";
                for (int i = 0; i < p; i++)
                {
                    ss += readBytes[i].ToString() + " ";
                }
                Console.WriteLine("===>" + ss);
            }
        }

        byte dt = 0xff;

        private byte getData()
        {
            byte tmp = 0;
            lock (this)
            {
                tmp = dt;
                dt = 0xff;
            }
            return tmp;
        }

        private byte waitCmd()
        {
            while (true)
            {
                byte ss = getData();
                if (ss != 0xff)// && ss.StartsWith("w"))
                    return ss;
                Thread.Sleep(1);
            }
        }
    }
}
