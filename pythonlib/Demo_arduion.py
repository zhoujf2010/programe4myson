'''
Created on 2020年2月2日

@author: zjf
'''

from Jimmylib import arduino
import time

if __name__ == '__main__':
    
    b = arduino()
    
#     for x in range(100):
#         b.setState(4, 1)
#         time.sleep(1)
#         b.setState(4, 0)
#         time.sleep(1)
    
#     pin = 9 
    while True:
        v = b.getState(3)
        print(v)
        b.setState(4, v)
#     
#     for x in range(100):
#         print(b.getState(7))
#         time.sleep(0.1)
# #     b.setHigh(pin)
# #     for x in range(10):
#         b.setHigh(pin)
#         time.sleep(0.1)
#         b.setLow(pin)
#     b.disconnect()

#     x = 2
#     while True:
#         prev = x -1 
#         if prev == 1:
#             prev = 9
#         
#         b.set(prev,False) 
#         b.set(x ,True)
#         
#         x = x + 1
#         if x == 10:
#             x = 2
        
#         time.sleep(0.01)
        
