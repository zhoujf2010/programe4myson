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

    
class WebSocketIO(object):
    '''
    classdocs
    '''

    def __init__(self, msgcallback):
        self.ws = ws = websocket.WebSocketApp("ws://localhost:55/scratch/bt",
        on_message=self.on_message,
        on_error=self.on_error,
        on_close=self.on_close)
        ws.on_open = self.on_open
        self.isstarted = False
        self.index = 0
        self.currentmsg1 = ""
        self.currentmsg2 = ""
        self.msgcallback = msgcallback
        
        def run(*args):
            print('started....')
            ws.run_forever()

        thread.start_new_thread(run, ())
        while not self.isstarted:
            time.sleep(0.00001)
            
#         while not self.isstarted:
#             time.sleep(0.00001)
        
    def on_message(self, message):
#         print("rec:", message)
        dt = json.loads(message)
        self.msgcallback(dt)
    
    def on_error(self, error):
        print(error)
    
    def on_close(self):
        print("### closed ###")
    
    def on_open(self):
        self.isstarted = True
        print("### opened ###")
        
    def sendcmd(self, cmd):
        index = self.index
        if index < 65535:
            index = index + 1;
        else:
            index = 1
        self.index = index
        msg = '{"jsonrpc":"2.0","method":"send","params":{"message":"%s","encoding":"base64"},"id":%d}' % (cmd, index)
        self.ws.send(msg)
#         print("send:" + msg)
        return index
    
    def sendConect(self, peripheralId):
        index = self.index
        if index < 65535:
            index = index + 1;
        else:
            index = 1
        self.index = index
        msg = '{"jsonrpc":"2.0","method":"connect","params":{"peripheralId":"%s"},"id":%d}' % (peripheralId, index)
        self.ws.send(msg)
#         print("send:" + msg)
        return index
    
    def sendDiscover(self):
        index = self.index
        if index < 65535:
            index = index + 1;
        else:
            index = 1
        self.index = index
        msg = '{"jsonrpc":"2.0","method":"discover","params":{"majorDeviceClass":8,"minorDeviceClass":1},"id":%d}' % (index)
        self.ws.send(msg)
#         print("send:" + msg)
        return index
    
    def sendtxt(self,txt):
        self.ws.send(txt)
#         print("send:" + txt)
        
    def send(self, msg):
        self.ws.send(msg)
#         print("send:" + msg)
    
    def disconnect(self):
        self.ws.close()
