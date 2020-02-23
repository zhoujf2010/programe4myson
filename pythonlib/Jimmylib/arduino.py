'''
Created on 2020年2月2日

@author: zjf
'''

from .common import WebSocketIO


class arduino(object):
    '''
    classdocs
    '''

    def __init__(self, port="COM3", baudrate=115200):
        self.io = WebSocketIO(self.msg, "hc")
        print("成功连接到代理器！")
        self._connect(port, baudrate)
        self._inputlst = []
        self._outputlst = []
    
    def msg(self, dt):
#         print(dt)
        pass
    
    def _connect(self, port, baudrate):    
        ret = self.io.sendmethod("connect", '{"port":"%s","baudrate":"%d"}' % (port, baudrate))
        if ret["result"] == "OK":
            print("Arduino连接成功")
        else:
            raise Exception(ret["msg"])
    
    def disconnect(self):   
        self.io.sendmethod("disconnect", '{}')
    
    def _setoutput(self, pin):
        self.__sendData('6')
        self._waitW()
        self.__sendData(pin)
        self._waitW()
    
    def _setinput(self, pin):
        self.__sendData('8')
        self._waitW()
        self.__sendData(pin)
        self._waitW()
    
    def setState(self, pin, val):
        if pin not in self._outputlst:
            self._setoutput(pin)
            self._outputlst.append(pin)
        if val == True or val == 1:
            self.setHigh(pin)
        else:
            self.setLow(pin)
    
    def setLow(self, pin):
        self.__sendData('0')
        self._waitW()
        self.__sendData(pin)
        self._waitW()
    
    def setHigh(self, pin):
        self.__sendData('1')
        self._waitW()
        self.__sendData(pin)
        self._waitW()

    def getState(self, pin):
        if pin not in self._inputlst:
            self._setinput(pin)
            self._inputlst.append(pin)
        self.__sendData('2')
        self._waitW()
        self.__sendData(pin)
        
        val = self._waitW()
        # 继续等待返回的值
        val = str.strip(val)
        while len(val) == 0:
            s = self.__readData()
            val = val + s
        return int(str.strip(val))
    
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

    def __sendData(self, serial_data):
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
        
