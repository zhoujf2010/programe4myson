'''
Created on 2020年2月2日

@author: zjf
'''

from .common import WebSocketIO
import base64


class arduino(object):
    '''
    classdocs
    '''

    def __init__(self, port="COM3", baudrate=115200):
        self.io = WebSocketIO(self.msg, "hc",'arduino')
        self._connect(port, baudrate)
        print("OK")
        self._inputlst = []
        self._outputlst = []
        #清空读入
        self.__sendData(3, 0, 0)
        self.currentmsg = 0
    
    def msg(self, dt):
#         print(dt)
        if "method" in dt  and dt["method"] == "hcval":
            msg =  dt["params"]["message"]
            self.currentmsg = msg
    
    def _connect(self, port, baudrate):    
        ret = self.io.sendmethod("connect", '{"port":"%s","baudrate":"%d"}' % (port, baudrate))
        if ret["result"] != "OK":
            raise Exception(ret["msg"])
    
    def disconnect(self):   
        self.io.sendmethod("disconnect", '{}')
    
    def _setoutput(self, pin):
        self.__sendData(0,1,pin)
    
    def _setinput(self, pin):
        self.__sendData(0,3,pin)
    
    def setState(self, pin, val):
        if pin not in self._outputlst:
            self._setoutput(pin)
            self._outputlst.append(pin)
        if val == True or val == 1:
            self.setHigh(pin)
        else:
            self.setLow(pin)
    
    def setLow(self, pin):
        self.__sendData(1,0,pin)
    
    def setHigh(self, pin):
        self.__sendData(1,1,pin)

    def getState(self, pin):
        if pin not in self._inputlst:
            self._setinput(pin)
            self.__sendData(3,1,pin) #设置pin为读取，不断反馈数据
            self._inputlst.append(pin)
        pos = self._inputlst.index(pin)
        
        val = self.currentmsg >> pos
        val = 0x01 & val
        
        if val > 0:
            return 1
        else:
            return 0
    
    def analogWrite(self, pin, value):
        pass
#         self.__sendData('3')
#         self.__sendData(pin)
#         self.__sendData(value)
#         return True
    
    def analogRead(self, pin):
        pass
#         self.__sendData('4')
#         self.__sendData(pin)
#         return self.__getData()

    def __sendData(self, cmd, param, pin):
        serial_data = (cmd << 6) | (param << 4) | pin
        self.io.sendmethod("send", '{"msg":"%s"}' % (serial_data))
    
    def _waitW(self):
        while True:
            v = self.__readData()
            if len(v) > 0 and v[0] == 'w':
                return v[1:]
       
    def __readData(self):
        ret = self.io.sendmethod("read", '{}') 
#         print('msg',ret)
        if ret["result"] == "Error":
            raise Exception(ret["msg"])
        return ret["msg"]
        
