# coding=utf-8
'''
Created on 2019年3月19日

@author: zjf
'''

from Jimmylib import wedo,arduino
import time

if __name__ == '__main__':
   
    hub = wedo()
#     b = arduino()
    # 电机测试
#     hub.turn_motor(50)
#     print(1)
#     time.sleep(4)
    for i in range(0,100):
        t = time.time()
        v = hub.get_object_distance()
        dt = time.time() - t;
        print(v,"用时:",dt / 1000.0)#,b.getState(4))
        time.sleep(0.1)
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
#     hub.motor_brake()

    # 距离传感器
#     time.sleep(2)
#     for i in range(100):
#         print(hub.get_object_distance())
#         time.sleep(0.1)
    
    #倾斜传感器
#     time.sleep(2)
#     for i in range(1000):
#         print(hub.get_tiltX() ,'   ', hub.get_tiltY())
#         time.sleep(0.1)

    # 两合
#     time.sleep(2)
#     for i in range(100):
#         print(hub.get_object_distance(), '  ', hub.get_tilt())
#         time.sleep(0.1)
        
#     hub.disconnect()
    
