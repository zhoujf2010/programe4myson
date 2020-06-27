#include <ESP8266WiFi.h>
#include <Ticker.h>

#define MAX_SRV_CLIENTS 3   //最大同时连接数，即你想要接入的设备数量，8266tcpserver只能接入五个，哎
WiFiServer server(8266);//你要的端口号，随意修改，范围0-65535
WiFiClient serverClients[MAX_SRV_CLIENTS];


const char *ssid     = "qinhh";//这里写入网络的ssid
const char *password = "58766730";//wifi密码

//static const uint8_t LED_Red = 2;
//static const uint8_t LED_Green = 2;
//static const uint8_t LED_Reset = 3;

static const uint8_t LED_Red = 12;
static const uint8_t LED_Green = 4;
static const uint8_t LED_Reset = 14;


Ticker flipper;

bool show = false;

void flip()
{
  if (show) {
    show = false;
    digitalWrite(LED_Red, HIGH); //红灯
  }
  else
  {
    show = true;
    digitalWrite(LED_Red, LOW); //红灯
  }
}

void setup() {

  Serial.begin(115200);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);


  pinMode(LED_Red, OUTPUT);
  pinMode(LED_Green, OUTPUT);

  flipper.attach(0.5, flip);//红灯闪动

  WiFi.begin(ssid, password);//启动

  //在这里检测是否成功连接到目标网络，未连接则阻塞。
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(100);
  }

  //几句提示
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.begin();
  server.setNoDelay(true);  //加上后才正常些

  flipper.detach();
  digitalWrite(LED_Red, HIGH);//绿灯常亮
}

void loop() {
  uint8_t i;
  if (server.hasClient())
  {
    for (i = 0; i < MAX_SRV_CLIENTS; i++)
    {
      if (!serverClients[i] || !serverClients[i].connected())
      {
        if (serverClients[i]) serverClients[i].stop();//未联接,就释放
        serverClients[i] = server.available();//分配新的
        continue;
      }
    }
    WiFiClient serverClient = server.available();
    serverClient.stop();
  }
  for (i = 0; i < MAX_SRV_CLIENTS; i++)
  {
    if (serverClients[i] && serverClients[i].connected())
    {
      if (serverClients[i].available())
      {
        while (serverClients[i].available()) {
          char v = serverClients[i].read();
          Serial.println(v);
          byte cmd = v >> 6 ;  //头两个为命令类型
          byte param = (v & 0x30) >> 4; //高四位中后两位为命令参数
          char pin = v & 0x0F;  //低四位为pin编号

          if (cmd == 0) { //设置PIN类型
            if (param == 1)
              pinMode(pin, OUTPUT);
            else if (param == 2)
              pinMode(pin, INPUT);
            else if (param == 3)
              pinMode(pin, INPUT_PULLUP);
          }
          else if (cmd == 1) { //写值
            if (param == 0)
              digitalWrite(pin, LOW);
            else if (param == 1)
              digitalWrite(pin, HIGH);
          }
          else if (cmd == 2) {//读值
            serverClients[i].print(digitalRead(pin));
          }
        }
      }
    }
  }
}
