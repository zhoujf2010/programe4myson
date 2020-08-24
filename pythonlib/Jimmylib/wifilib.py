'''
Created on 2020年6月27日

@author: zjf
'''
import socket
import threading

class MyWifi(object):
    '''
    wifi控制
    '''


    def __init__(self, ip,port,reccallback=None):
        self.ip = ip
        self.port = port
        self._inputlst = []
        self._outputlst = []
        self.open()
        if reccallback != None:
            self.reccallback = reccallback
            t = threading.Thread(target=self.resv)
            self.BUF_SIZE = 1024
            t.start()
    
    def open(self):
        self.s = socket.socket() 
        self.s.connect((self.ip, self.port))
    
    def send(self,msg):
        self.s.send(bytes(msg,'utf-8'))
        
    def close(self):
        self.s.close()
        
    def resv(self):
        try:
            while True:
                data = self.s.recv(self.BUF_SIZE)
                text = data.decode()
                self.reccallback(text)
        except :
            pass
    
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
            
        
        