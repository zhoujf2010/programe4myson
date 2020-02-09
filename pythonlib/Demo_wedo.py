# coding=utf-8
'''
Created on 2019年3月19日

@author: zjf
'''

from Jimmylib import wedo
import time

if __name__ == '__main__':
   
    hub = wedo()
    # 电机测试
    hub.turn_motor(50)
    print(1)
    time.sleep(5)
#     hub.turn_motor(60)
#     time.sleep(2)
#     hub.turn_motor(40)
#     time.sleep(2)
#     hub.motor_brake()
#     time.sleep(2)
#     hub.turn_motor(-40)
#     time.sleep(2)
#     hub.turn_motor(-100)
#     time.sleep(2)
    hub.motor_brake()

    # 距离传感器
#     time.sleep(2)
#     for i in range(100):
#         print(hub.get_object_distance())
#         time.sleep(0.1)
    
    #倾斜传感器
    time.sleep(2)
    for i in range(1000):
        print(hub.get_tiltX() ,'   ', hub.get_tiltY())
        time.sleep(0.1)

    # 两合
#     time.sleep(2)
#     for i in range(100):
#         print(hub.get_object_distance(), '  ', hub.get_tilt())
#         time.sleep(0.1)
        
#     hub.disconnect()
    
