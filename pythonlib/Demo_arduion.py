'''
Created on 2020年2月2日

@author: zjf
'''

from Jimmylib import arduino
import time

if __name__ == '__main__':
    
    a = arduino()
    
    for x in range(1000000):
        # a.setState(8, 1)
        # time.sleep(1)
        # a.setState(8, 0)
        # time.sleep(1)
        # print(a.getState(2),a.getState(3),a.getState(4),a.getState(5),a.getState(6),a.getState(7),a.getState(8))
        # time.sleep(0.5)
        a.setHigh(2)
        time.sleep(1)
        a.setLow(2)
        time.sleep(1)                              
    
#     pin = 9 
#     while True:
#         t = time.time()
#         v4 = a.getState(4)
#         v5 = a.getState(5)
#         v6 = a.getState(6)
#         v2 = a.getState(2)
#         v8 = a.getState(8)
#         v3 = a.getState(3)
#         v7 = a.getState(7)
# #         v4 = a.getState(5)
# #         v5 = a.getState(6)
# #         print(v)
#         dt = time.time() - t;
#         print(v6,v7,v8,v2,v3,v4,v5,"用时:",dt / 1000.0)#,b.getState(4))
#         time.sleep(0.1)
#         #a.setState(12, 1- v)




#     while True:
        
# #         i = 2
# #         while i <= 8:
# #             p = i-1
# #             if p == 1:
# #                 p = 10;
# #             a.setState(p,0)
# #             a.setState(i,1)
# #             a.setState(i+1,1)
# #             i = i+1   
# #             time.sleep(0.05)
        
#         for i in range(9,13):
#             a.setState(i,1)
# #             time.sleep(0.01)
             
#         time.sleep(0.1)
     
#         for i in range(9,13):
#             a.setState(i,0)
             
#         time.sleep(0.1)

# #         v = b.getState(3)
# #         print(v)
# #         b.setState(4, v)
# #     
# #     for x in range(100):
# #         print(b.getState(7))
# #         time.sleep(0.1)
# # #     b.setHigh(pin)
# # #     for x in range(10):
# #         b.setHigh(pin)
# #         time.sleep(0.1)
# #         b.setLow(pin)
# #     b.disconnect()

# #     x = 2
# #     while True:
# #         prev = x -1 
# #         if prev == 1:
# #             prev = 9
# #         
# #         b.set(prev,False) 
# #         b.set(x ,True)
# #         
# #         x = x + 1
# #         if x == 10:
# #             x = 2
        
# #         time.sleep(0.01)
        
