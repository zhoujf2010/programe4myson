'''
Created on 2019年3月21日

@author: zjf
'''
import websocket
import json
import time
import base64

try:
    import thread
except ImportError:
    import _thread as thread
    
class WebSocketIO2(object):
    '''
    classdocs
    '''
    def __init__(self, msgcallback):
        self.ws = ws = websocket.WebSocketApp("ws://localhost:55/scratch/ble",
        on_message=self.on_message,
        on_error=self.on_error,
        on_close=self.on_close)
        ws.on_open = self.on_open
        self.isstarted = False
        self.index = 1
        self.currentmsg1 = ""
        self.currentmsg2 = ""
        self.msgcallback = msgcallback
        
        def run(*args):
            print('started....')
            ws.run_forever()

        thread.start_new_thread(run, ())
        while not self.isstarted:
            time.sleep(0.00001)
        
        
    def on_message(self, message):
#         print("rec:", message)
        dt = json.loads(message)
        if "method" in dt  and dt["method"] == "characteristicDidChange":
            if dt["params"]["characteristicId"].startswith("00001560") >0 :
                msg =  dt["params"]["message"]
                data = base64.b64decode(msg)
                if data[1] == 1:
                    self.currentmsg1 = data
                elif data[1] == 2:
                    self.currentmsg2 = data
        self.msgcallback(dt)
    
    def on_error(self, error):
        print(error)
    
    def on_close(self):
        print("### closed ###")
    
    def on_open(self):
        self.isstarted = True
        print("### opened ###")
        
    def sendcmd(self, cmd):
        s = base64.b64encode(bytes(cmd))
        index = self.index
        index = index + 1;
        self.index = index
        msg = '{"jsonrpc":"2.0","method":"write","params":{"serviceId":"00004f0e-1212-efde-1523-785feabcd123","characteristicId":"00001565-1212-efde-1523-785feabcd123","message":"%s","encoding":"base64"},"id":%d}'%(str(s,'utf-8'),index)
        self.ws.send(msg)
        print("Send:"+msg)
        
    def sendcmd2(self,casid, cmd):
        s = base64.b64encode(bytes(cmd))
        index = self.index
        index = index + 1;
        self.index = index
        casid = casid.lower()
        msg = '{"jsonrpc":"2.0","method":"write","params":{"serviceId":"00004f0e-1212-efde-1523-785feabcd123","characteristicId":"%s","message":"%s","encoding":"base64"},"id":%d}'%(casid,str(s,'utf-8'),index)
        self.ws.send(msg)
#         print("Send:"+msg)
        
#     def sendcmd2(self, casid, cmd):
#         s = base64.b64encode(bytes(cmd))
#         index = self.index
#         index = index + 1;
#         self.index = index
#         msg = '{"jsonrpc":"2.0","method":"read","params":{"serviceId":"00004f0e-1212-efde-1523-785feabcd123","characteristicId":"%s","message":"%s","encoding":"base64"},"id":%d}'%(casid,str(s,'utf-8'),index)
#         self.ws.send(msg)
    
    def sendtxt(self,txt):
        self.ws.send(txt)
#         print("Send:"+txt)
        
    def disconnect(self):
        # adapter.stop()
        self.ws.close()
        
    def getCurrentmsg(self,connect_id):
        if connect_id == 1:
            return self.currentmsg1
        elif connect_id ==2:
            return self.currentmsg2
        print('-------------')
        return None
        
