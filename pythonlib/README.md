Jimmylib主要用于python访问相关设备的代码，  
其中包括，乐高的wedo，乐高的ev3，arduino，语音处理等，方便孩子直接拿来使用。  
硬件设备需要与scratch_link程序配合使用  
大多代码引入三方github库，在此感谢作者的支持：  
EV3 :   
- https://github.com/ev3dev/ev3dev-lang-python
- https://www.lego.com/cdn/cs/set/assets/blt77bd61c3ac436ea3/LEGO_MINDSTORMS_EV3_Firmware_Developer_Kit.pdf
- https://www.wolfcstech.com/2018/10/30/lego_ev3_direct_command_003/  

&emsp;&emsp;修改点： 将代码改为scarch_link来驱动ev3设备

wedo:  
- https://github.com/jannopet/LEGO-WeDo-2.0-Python-SDK

&emsp;&emsp;修改点：重构了一下代码

arduino:
- https://github.com/HashNuke/Python-Arduino-Prototyping-API

&emsp;&emsp;修改点： 改成了通过scarch_link，然后让arduino通过HC06蓝牙接口进行通讯




