'''
Created on 2020年2月9日

@author: zjf
'''

from Jimmylib import myVoice

if __name__ == '__main__':
    v = myVoice()
    while True:
        print("listing...")
        print(v.getVoice())
        #v.playVoice("你好啊")
        print("OK")