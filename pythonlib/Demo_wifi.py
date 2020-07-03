'''
Created on 2020年6月27日

@author: zjf
'''
from Jimmylib import MyWifi
import time

if __name__ == '__main__':
    wifi = MyWifi("192.168.3.106",8266)
    wifi.setState(12,0)
    while True:
        wifi.setState(5,1)
        time.sleep(0.5)
        wifi.setState(5,0)
        time.sleep(0.5)


