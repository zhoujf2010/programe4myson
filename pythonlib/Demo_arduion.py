'''
Created on 2020年2月2日

@author: zjf
'''

from Jimmylib import arduino
import time

if __name__ == '__main__':
    
    a = arduino()
    
#     for x in range(100):
#         b.setState(4, 1)
#         time.sleep(1)
#         b.setState(4, 0)
#         time.sleep(1)
    
#     pin = 9 
    while True:
        v = a.getState(10)
#         print(v)
        a.setState(2, 1- v)




    while True:
        
#         i = 2
#         while i <= 8:
#             p = i-1
#             if p == 1:
#                 p = 10;
#             a.setState(p,0)
#             a.setState(i,1)
#             a.setState(i+1,1)
#             i = i+1   
#             time.sleep(0.05)
        
        for i in range(2,10):
            a.setState(i,1)
#             time.sleep(0.01)
             
        time.sleep(0.1)
     
        for i in range(2,10):
            a.setState(i,0)
             
        time.sleep(0.1)

#         v = b.getState(3)
#         print(v)
#         b.setState(4, v)
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
        
