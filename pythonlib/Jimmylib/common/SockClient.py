'''
Created on 2019年3月21日

@author: zjf
'''
import websocket
import json
import time
import base64
import sys
import os
import psutil   
import socket

import threading




class SockClient(threading.Thread):

    def __init__(self,msgcallback, host_ip, host_port):
        threading.Thread.__init__(self)
        self.running = False
        self.msgcallback = msgcallback
        self.sock = socket.socket()
        self.sock.settimeout(20)  # 20 seconds
        try:
            self.sock.connect((host_ip, host_port))
            self.sock.settimeout(None)
        except socket.error as e:
            print("Socket Connect Error:%s" % e)
            exit(1)
        self.running = True

        self.error_cnt = 0

    def run(self):
        while self.running:
            try:
                data = self.sock.recv(1)
                if len(data) > 0:
                    self.error_cnt = 0
                    #recv_data = data.encode('hex')
                    #print('recv:', data)
                    dt ={"method":"hcval","params":{"message":data[0]}}
                    self.msgcallback(dt)
            except socket.error as e:
                print('socket running error:', str(e))
                break

        print('SockClient Thread Exit\n')

    
    def sendcmd(self, cmd):
        self.sock.send(cmd.encode())

    def sendmethod(self,method, param):
        dt = json.loads(param)
        data = int(dt["msg"])
        # print(data)
        my_bytes = bytearray()
        my_bytes.append(data)

        self.sock.send(my_bytes)
