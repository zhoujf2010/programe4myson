# coding=utf-8
'''
Created on 2019年3月19日

@author: zjf
'''

from Jimmylib import ev3
import time

if __name__ == '__main__':
    ev3 = ev3()
    print(0)
    ev3.testSendcmd()
    for i in range(1,10):
        ev3.MotorOn(ev3.PORT_A, (i * 10))
        time.sleep(1)
    ev3.MotorOff(ev3.PORT_A)
    
#     ev3.testsound()
#     ev3.MotorOn(ev3.PORT_D, 50)
#     print(1)
#     time.sleep(3)
#     ev3.MotorOff(ev3.PORT_A)
    
#     ev3.disconnect()
    
