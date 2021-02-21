'''
Created on 2020年2月2日

@author: zjf
'''

from Jimmylib import arduino2
import time

import sys

import socket

import threading

from time import sleep


class SockClient(threading.Thread):

    def __init__(self, host_ip, host_port):
        threading.Thread.__init__(self)
        self.running = False
        self.sock = socket.socket()
        self.sock.settimeout(20)  # 20 seconds
        try:
            self.sock.connect((host_ip, host_port))
        except socket.error as e:
            print("Socket Connect Error:%s" % e)
            exit(1)
        print("connect success")
        self.running = True

        self.error_cnt = 0

    def run(self):

        while self.running:

            try:
                send_data = b'\x12\x34\x56'
                self.sock.send('aaa\r\nbb'.encode())
                data = self.sock.recv(1024)
                if len(data) > 0:
                    self.error_cnt = 0
                    print('recv:', data)

                sleep(1)

            except socket.error as e:
                print('socket running error:', str(e))
                break

        print('SockClient Thread Exit\n')


if __name__ == '__main__':
    
    print(1)
    a = arduino2()
    # for i in range(0,100):
    #     a.setHigh(2)
    #     time.sleep(1)
    #     a.setLow(2)
    #     time.sleep(1)
    for i in range(0,100):
        print(a.getState(3))
        time.sleep(0.1)
    time.sleep(30)
    
    # sock_client = SockClient('192.168.3.170', 8080)
3
    # sock_client.start()

    # try:
    #     while True:
    #         sleep(1)

    #         if not sock_client.is_alive():
    #             break

    # except KeyboardInterrupt:
    #     print('ctrl+c')
    #     sock_client.running = False

    # sock_client.join()
    # print('exit finally')
