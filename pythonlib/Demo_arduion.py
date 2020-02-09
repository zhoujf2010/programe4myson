'''
Created on 2020年2月2日

@author: zjf
'''

from Jimmylib import arduino
import time

if __name__ == '__main__':
    b = arduino()
    pin = 9 
    b._setoutput(9)
    b._setinput(7)
    
    for x in range(100):
        print(b.getState(7))
        time.sleep(0.1)
#     b.setHigh(pin)
#     for x in range(10):
        b.setHigh(pin)
        time.sleep(0.1)
        b.setLow(pin)
#     b.disconnect()
