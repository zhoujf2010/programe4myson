'''
Created on 2020年6月27日

@author: zjf
'''
import socket

class MyWifi(object):
    '''
    wifi控制
    '''


    def __init__(self, ip,port):
        self.ip = ip
        self.port = port
        self._inputlst = []
        self._outputlst = []
        self.open()
    
    def open(self):
        self.s = socket.socket() 
        self.s.connect((self.ip, self.port))
    
    def send(self,msg):
        self.s.send(bytes(msg,'utf-8'))
    
    def __sendData(self, cmd, param, pin):
        data = (cmd << 6) | (param << 4) | pin
        print(chr(data))
        self.send(chr(data))
    
    def _setoutput(self,pin):
        self.__sendData(0,1,pin)
        
    def setLow(self, pin):
        self.__sendData(1,0,pin)
    
    def setHigh(self, pin):
        self.__sendData(1,1,pin)
        
    def setState(self, pin, val):
        if pin not in self._outputlst:
            self._setoutput(pin)
            self._outputlst.append(pin)
        if val == True or val == 1:
            self.setHigh(pin)
        else:
            self.setLow(pin)
            
        
        