# coding=utf-8
'''
Created on 2019年6月2日

@author: zjf
'''
from .common import WebSocketIO
import time
import struct
import datetime
import base64
import threading
from .common import const


class ev3(object):
    '''
    EV3 device,connected by scratch_link
    '''
    PORT_A = 1
    PORT_B = 2
    PORT_C = 4
    PORT_D = 8
    PORT_1 = b'\x00'
    PORT_2 = b'\x01'
    PORT_3 = b'\x02'
    PORT_4 = b'\x03'
    PORTS_ALL = 15

    def __init__(self):
        self._lock = threading.Lock()
        self.waitMap = {}
        self.waitidMap = {}
        self._msg_cnt = 0
        self.peripheralId = ""
        ws = WebSocketIO(self.msg,"bt")
        self.io = ws
        self._connect()  # connect throw websocket
        self._sync_mode = const.STD
        self._verbosity = 0
    
    def msg(self, dt):
        global peripheralId
#         print("rec:" + str(dt))
        if "method" in dt:
            if dt["method"] == "didDiscoverPeripheral":
                self.peripheralId = dt["params"]["peripheralId"]
            if dt["method"] == "didReceiveMessage":
                msg = dt["params"]["message"]
                t = base64.b64decode(msg)
                idval = t[2:4]
                if idval in self.waitMap.keys():
                    self.waitMap[idval] = t
        if "id" in dt:
            idval = dt["id"]
            if idval in self.waitidMap.keys():
                self.waitidMap[idval] = dt["result"]
                
    def _connect(self):    
        # 发现设备
        id = self.io.sendDiscover()
        while self.peripheralId == "":
            time.sleep(0.00001)
        self.waitidMap[2] = 'wait'
        self.io.sendConect(self.peripheralId)
        while self.waitidMap[2] == 'wait':  # 等待反馈
            time.sleep(0.00001)
        print("connected")       
    
    def disconnect(self):
        self.io.disconnect()
        
    def port_input(self, port_output: int) -> bytes:
        """
        get corresponding input motor port (from output motor port)
        """
        if port_output == self.PORT_1:
            return self.LCX(0)
        elif port_output == self.PORT_2:
            return self.LCX(1)
        elif port_output == self.PORT_3:
            return self.LCX(2)
        elif port_output == self.PORT_4:
            return self.LCX(3)
        elif port_output == self.PORT_A:
            return self.LCX(16)
        elif port_output == self.PORT_B:
            return self.LCX(17)
        elif port_output == self.PORT_C:
            return self.LCX(18)
        elif port_output == self.PORT_D:
            return self.LCX(19)
        else:
            raise ValueError("port_output needs to be one of the port numbers [1, 2, 4, 8]")
        
    def MotorOn(self, port, speed):
        ops = b''.join([
        const.opOutput_Power,
        self.LCX(0),  # LAYER
        self.LCX(port),  # NOS
        self.LCX(speed)
        ])
        self.send_direct_cmd(ops)  # , global_mem=8)
        
        ops = b''.join([
            const.opOutput_Start,
            self.LCX(0),  # LAYER
            self.LCX(port),  # NOS
        ])
        self.send_direct_cmd(ops)  # , global_mem=8)
    
    def MotorOff(self, port, brake=True):
        ops = b''.join([
            const.opOutput_Stop,
            self.LCX(0),  # LAYER
            self.LCX(port),  # NOS
            self.LCX(1 if brake else 0)
            ])
        self.send_direct_cmd(ops)  # , global_mem=8)
        
    def MotorOndegrees(self, port, speed, degrees, brake=True):
        ops = b''.join([
            const.opOutput_Step_Power,
            self.LCX(0),  # LAYER
            self.LCX(port),  # NO
            self.LCX(speed),  # power
            self.LCX(0),  # ramp_up
            self.LCX(degrees),  # degrees
            self.LCX(0),  # ramp_down
            self.LCX(1 if brake else 0),  # stop
            ])
        self.send_direct_cmd(ops)  # , global_mem=8)
        
        ops = b''.join([
            const.opOutput_Start,
            self.LCX(0),  # LAYER
            self.LCX(port),  # NOS
        ])
        self.send_direct_cmd(ops)  # , global_mem=8)
        
    def MotorPosition(self, port):
        ops = b''.join([
            const.opInput_Device,
            const.READY_RAW,
            self.LCX(0),  # LAYER
            self.port_input(port),  # NO
            self.LCX(7),  # TYPE - EV3-Large-Motor
            self.LCX(1),  # MODE - Degree
            self.LCX(1),  # VALUES
            self.GVX(0),  # VALUE1
            ])
        reply = self.send_direct_cmd(ops, global_mem=4)
        (pos,) = struct.unpack('<i', reply[5:])
        return pos
    
    def MotorPositionReset(self, port):
        ops = b''.join([
            const.opInput_Device,
            const.READY_RAW,
            self.LCX(0),  # LAYER
            self.port_input(port),  # NO
            self.LCX(7),  # TYPE - EV3-Large-Motor
            self.LCX(1),  # MODE - Degree
            self.LCX(1),  # VALUES
            self.GVX(0),  # VALUE1
            ])
        reply = self.send_direct_cmd(ops, global_mem=4)
        (pos,) = struct.unpack('<i', reply[5:])
        return pos
    
    '''
    读取模式
    '''

    def ReadModeType(self, port):
        ops = b''.join([
            const.opInput_Device,
            const.GET_TYPEMODE,
            self.LCX(0),  # LAYER
            self.port_input(port),  # NO
            self.GVX(0),  # TYPE
            self.GVX(1)  # MODE
        ])
        reply = self.send_direct_cmd(ops, global_mem=2)
        (tp, mode) = struct.unpack('BB', reply[5:])
        print("type: {}, mode: {}".format(tp, mode))
        
    def Ultrasonic_distance(self, port):
        """
        超声波距离传感器
        """
        ops = b''.join([
            const.opInput_Device,
            const.READY_RAW,
            self.LCX(0),  # LAYER
            self.port_input(port),  # NO
            self.LCX(30),  # TYPE - Ultrasonic
            self.LCX(0),  # MODE - cm
            self.LCX(1),  # VALUES
            self.GVX(0),  # VALUE1
            ])
        reply = self.send_direct_cmd(ops, global_mem=4)
        (pos,) = struct.unpack('<i', reply[5:])
        return pos
    
    '''
    按钮按下
    '''

    def Touch_ispressed(self, port):
        ops = b''.join([
            const.opInput_Device,
            const.READY_RAW,
            self.LCX(0),  # LAYER
            self.port_input(port),  # NO
            self.LCX(16),  # TYPE - Ultrasonic
            self.LCX(0),  # MODE - cm
            self.LCX(1),  # VALUES
            self.GVX(0),  # VALUE1
            ])
        reply = self.send_direct_cmd(ops, global_mem=4)
        (val,) = struct.unpack('<i', reply[5:])
        return val > 100
    
    def Touch_wait4pressed(self, port, timeout_ms=None, sleep_ms=10):
        """
        等待按钮按钮
        """
        return self._wait(True, port, timeout_ms, sleep_ms)
    
    def Touch_wait4released(self, port, timeout_ms=None, sleep_ms=10):
        """
        等待按钮释放
        """
        return self._wait(False, port, timeout_ms, sleep_ms)
    
    def Touch_wait4bump(self, timeout_ms=None, sleep_ms=10):
        """
        Wait for the touch sensor to be pressed down and then released.
        Both actions must happen within timeout_ms.
        """
        start_time = time.time()

        if self.wait_for_pressed(timeout_ms, sleep_ms):
#             if timeout_ms is not None:
#                 timeout_ms -= int((time.time() - start_time) * 1000)
            return self.wait_for_released(timeout_ms, sleep_ms)

        return False
    
    def _wait(self, wait_for_press, port, timeout_ms, sleep_ms):
        tic = time.time()

        if sleep_ms:
            sleep_ms = float(sleep_ms / 1000)
        while True:
            if self.Touch_ispressed(port) == wait_for_press:
                return True
            if timeout_ms is not None and time.time() >= tic + timeout_ms * 1000:
                return False
            if sleep_ms:
                time.sleep(sleep_ms)
                
    def color_ambient(self, port):
        '''
        获取环境光强(0~100),传感器显蓝色
        '''
        ops = b''.join([
            const.opInput_Device,
            const.READY_RAW,
            self.LCX(0),  # LAYER
            self.port_input(port),  # NO
            self.LCX(29),  # TYPE - Ultrasonic
            self.LCX(1),  # MODE - cm
            self.LCX(1),  # VALUES
            self.GVX(0),  # VALUE1
            ])
        reply = self.send_direct_cmd(ops, global_mem=4)
        (val,) = struct.unpack('<i', reply[5:])
        return val        
                
    def color_reflected(self, port):
        '''
        获取反射光强(0~100),传感器显红色
        '''
        ops = b''.join([
            const.opInput_Device,
            const.READY_RAW,
            self.LCX(0),  # LAYER
            self.port_input(port),  # NO
            self.LCX(29),  # TYPE - Ultrasonic
            self.LCX(0),  # MODE - cm
            self.LCX(1),  # VALUES
            self.GVX(0),  # VALUE1
            ])
        reply = self.send_direct_cmd(ops, global_mem=4)
        (val,) = struct.unpack('<i', reply[5:])
        return val      
    
    def getColName(self, value):
        COLORS = (
          'NoColor',
          'Black',
          'Blue',
          'Green',
          'Yellow',
          'Red',
          'White',
          'Brown',
        )
        return COLORS[value]
                
    def color_detect(self, port):
        '''
        探测颜色 
          - 0: No color
          - 1: Black
          - 2: Blue
          - 3: Green
          - 4: Yellow
          - 5: Red
          - 6: White
          - 7: Brown
        '''
        ops = b''.join([
            const.opInput_Device,
            const.READY_RAW,
            self.LCX(0),  # LAYER
            self.port_input(port),  # NO
            self.LCX(29),  # TYPE - Ultrasonic
            self.LCX(2),  # MODE - cm
            self.LCX(1),  # VALUES
            self.GVX(0),  # VALUE1
            ])
        reply = self.send_direct_cmd(ops, global_mem=4)
        (val,) = struct.unpack('<i', reply[5:])
        return val
    
#     def Gyro_reset(self,port):
#         """
#         陀螺仪，重置
#         """
#         ops = b''.join([
#             const.opInput_Device,
#             const.READY_RAW,
#             self.LCX(0),  # LAYER
#             self.port_input(port),  # NO
#             self.LCX(32),  # TYPE - Ultrasonic
#             self.LCX(4),  # MODE - cm
#             self.LCX(1),  # VALUES
#             self.GVX(0),  # VALUE1
#             ])
#         reply = self.send_direct_cmd(ops, global_mem=4)
#         (val,) = struct.unpack('<i', reply[5:])
#         return val
    
    def Gyro_angle(self, port):
        """
        陀螺仪，角度测量(测量按箭头图示旋转角度)
        """
        ops = b''.join([
            const.opInput_Device,
            const.READY_RAW,
            self.LCX(0),  # LAYER
            self.port_input(port),  # NO
            self.LCX(32),  # TYPE - Ultrasonic
            self.LCX(0),  # MODE - cm
            self.LCX(1),  # VALUES
            self.GVX(0),  # VALUE1
            ])
        reply = self.send_direct_cmd(ops, global_mem=4)
        (val,) = struct.unpack('<i', reply[5:])
        return val
    
    def Gyro_rate(self, port):
        """
        陀螺仪，角度速度测量 度/秒
        """
        ops = b''.join([
            const.opInput_Device,
            const.READY_RAW,
            self.LCX(0),  # LAYER
            self.port_input(port),  # NO
            self.LCX(32),  # TYPE - Ultrasonic
            self.LCX(1),  # MODE - cm
            self.LCX(1),  # VALUES
            self.GVX(0),  # VALUE1
            ])
        reply = self.send_direct_cmd(ops, global_mem=4)
        (val,) = struct.unpack('<i', reply[5:])
        return val
    
    def Gyro_angle_rate(self, port):
        """
        陀螺仪，角度速度测量 度/秒
        """
        ops = b''.join([
            const.opInput_Device,
            const.READY_RAW,
            self.LCX(0),  # LAYER
            self.port_input(port),  # NO
            self.LCX(32),  # TYPE - Ultrasonic
            self.LCX(3),  # MODE - cm
            self.LCX(1),  # VALUES
            self.GVX(0),  # VALUE1
            ])
        reply = self.send_direct_cmd(ops, global_mem=8)
        val = struct.unpack('<ii', reply[5:])
        return val

    def playSound(self, FREQUENCY, DURATION, VOLUME=100):
        """
    播放一段音调
        """
        ops = b''.join([
            const.opSound,
            const.TONE,
            self.LCX(VOLUME),  # VOLUME
            self.LCX(FREQUENCY),  # FREQUENCY
            self.LCX(DURATION),  # DURATION
        ])
        self.send_direct_cmd(ops)
        
    def playSoundFile(self, filename, VOLUME=100):
        """
                    播放上传的Sounds工程下的声音文件
        """
        ops = b''.join([
            const.opSound,
            const.PLAY,
            self.LCX(VOLUME),  # VOLUME
            self.LCS('../prjs/Sounds/' + filename)  # First character in filename
        ])
        self.send_direct_cmd(ops)
        
    def displayImage(self, filename):
        """
                  显示图片
        """
        if filename == '':
            ops = b''.join([
                const.opUI_Draw,
                const.FILLWINDOW,
                self.LCX(0),  # COLOR
                self.LCX(0),  # Y0
                self.LCX(0),  # Y1
                const.opUI_Draw,
                const.UPDATE
            ])
        else:
            ops = b''.join([
                const.opUI_Draw,
                const.TOPLINE,
                self.LCX(0),  # ENABLE
                const.opUI_Draw,
                const.BMPFILE,
                self.LCX(1),  # COLOR
                self.LCX(0),  # X0
                self.LCX(0),  # Y0
                self.LCS("../prjs/Images/" + filename + ".rgf"),  # NAME
                const.opUI_Draw,
                const.UPDATE
            ])
        self.send_direct_cmd(ops)

    def testsound(self):
#         ops = b''.join([
#             const.opSound,
#             const.TONE,
#             self.LCX(1),  # VOLUME
#             self.LCX(440),  # FREQUENCY
#             self.LCX(1000),  # DURATION
#         ])
#         ops = b''.join([
#             const.opSound,
#             const.PLAY,
#             self.LCX(100),  # VOLUME
# #             self.LCS('./BrkDL_SAVE/Activate')  # First character in filename
#             self.LCS('../prjs/Sounds/Seven')  # First character in filename
#         ])
#         self.send_direct_cmd(ops)
        ops = b''.join([
            const.opUI_Draw,
            const.TOPLINE,
            self.LCX(0),  # ENABLE
            const.opUI_Draw,
            const.BMPFILE,
            self.LCX(1),  # COLOR
            self.LCX(0),  # X0
            self.LCX(0),  # Y0
#             self.LCS("../apps/Motor Control/MotorCtlAD.rgf"), # NAME
            self.LCS("../prjs/Images/Color sensor.rgf"),  # NAME
            const.opUI_Draw,
            const.UPDATE
        ])
#         ops = b''.join([
#             const.opUI_Draw,
#             const.TOPLINE,
#             self.LCX(1),     # ENABLE
#             const.opUI_Draw,
#             const.FILLWINDOW,
#             self.LCX(0),     # COLOR
#             self.LCX(0),     # Y0
#             self.LCX(0),     # Y1
#             const.opUI_Draw,
#             const.UPDATE
#         ])
        self.send_direct_cmd(ops)
    
    '''
    加载EV3文件夹
    '''

    def getSubDirlist(self, directory):
        ops = b''.join([
            const.opFile,
            const.GET_FOLDERS,
            self.LCS(directory),
            self.GVX(0)
        ])
        reply = self.send_direct_cmd(ops, global_mem=1)
        num = struct.unpack('<B', reply[5:])[0]
        print("Directory '{}' has {} subdirectories:".format(directory, num))
        for i in range(num):
            ops = b''.join([
                const.opFile,
                const.GET_SUBFOLDER_NAME,
                self.LCS(directory),
                self.LCX(i + 1),  # ITEM
                self.LCX(64),  # LENGTH
                self.GVX(0)  # NAME
            ])
            reply = self.send_direct_cmd(ops, global_mem=64)
            subdir = struct.unpack('64s', reply[5:])[0]
            subdir = subdir.split(b'\x00')[0]
            subdir = subdir.decode("utf8")
            print("  {}".format(subdir))
        
    def testSendcmd(self):
        ops = const.opNop
        self.verbosity = 1
     
        print("*** SYNC ***")
        self.sync_mode = const.SYNC
        self.send_direct_cmd(ops)
        print("*** ASYNC (no reply) ***")
        self.sync_mode = const.ASYNC
        self.send_direct_cmd(ops)
        
        print("*** ASYNC (reply) ***")
        counter_1 = self.send_direct_cmd(ops, global_mem=1)
        counter_2 = self.send_direct_cmd(ops, global_mem=1)
        self.wait_for_reply(counter_1)
        self.wait_for_reply(counter_2)
        
        print("*** STD (no reply) ***")
        self.sync_mode = const.STD
        self.send_direct_cmd(ops)
        
        print("*** STD (reply) ***")
        self.send_direct_cmd(ops, global_mem=5)
        self.send_direct_cmd(ops, global_mem=5)
    
    @property
    def sync_mode(self) -> str:
        """
        sync mode (standard, asynchronous, synchronous)
        STD:   Use DIRECT_COMMAND_REPLY if global_mem > 0,
               wait for reply if there is one.
        ASYNC: Use DIRECT_COMMAND_REPLY if global_mem > 0,
               never wait for reply (it's the task of the calling program).
        SYNC:  Always use DIRECT_COMMAND_REPLY and wait for reply.
        The general idea is:
        ASYNC: Interruption or EV3 device queues direct commands,
               control directly comes back.
        SYNC:  EV3 device is blocked until direct command is finished,
               control comes back, when direct command is finished.
        STD:   NO_REPLY like ASYNC with interruption or EV3 queuing,
               REPLY like SYNC, synchronicity of program and EV3 device.
        """
        return self._sync_mode

    @sync_mode.setter
    def sync_mode(self, value: str):
        assert isinstance(value, str), \
            "sync_mode needs to be of type str"
        assert value in [const.STD, const.SYNC, const.ASYNC], \
            "value of sync_mode: " + value + " is invalid"
        self._sync_mode = value
        
    @property
    def verbosity(self) -> int:
        """
        level of verbosity (prints on stdout).
        """
        return self._verbosity

    @verbosity.setter
    def verbosity(self, value:int):
        assert isinstance(value, int), \
            "verbosity needs to be of type int"
        assert value >= 0 and value <= 2, \
            "allowed verbosity values are: 0, 1 or 2"
        self._verbosity = value
    
    def LCX(self, value: int) -> bytes:
        """create a LC0, LC1, LC2, LC4, dependent from the value"""
        if   value >= -32 and value < 0:
            return struct.pack('b', 0x3F & (value + 64))
        elif value >= 0 and value < 32:
            return struct.pack('b', value)
        elif value >= -127 and value <= 127:
            return b'\x81' + struct.pack('<b', value)
        elif value >= -32767 and value <= 32767:
            return b'\x82' + struct.pack('<h', value)
        else:
            return b'\x83' + struct.pack('<i', value)
        
    def LCS(self, value: str) -> bytes:
        """
        pack a string into a LCS
        """
        return b'\x84' + str.encode(value) + b'\x00'

    def GVX(self, value: int) -> bytes:
        """create a GV0, GV1, GV2, GV4, dependent from the value"""
        if value < 0:
            raise RuntimeError('No negative values allowed')
        elif value < 32:
            return struct.pack('<b', 0x60 | value)
        elif value < 256:
            return b'\xe1' + struct.pack('<b', value)
        elif value < 65536:
            return b'\xe2' + struct.pack('<h', value)
        else:
            return b'\xe3' + struct.pack('<i', value)

    def port_motor_input(self, port_output: int) -> bytes:
        """
        get corresponding input motor port (from output motor port)
        """
        if port_output == const.PORT_A:
            return self.LCX(16)
        elif port_output == const.PORT_B:
            return self.LCX(17)
        elif port_output == const.PORT_C:
            return self.LCX(18)
        elif port_output == const.PORT_D:
            return self.LCX(19)
        else:
            raise ValueError("port_output needs to be one of the port numbers [1, 2, 4, 8]")

    def Send(self, msg):
        return self.io.sendcmd(msg)
    
    def send_direct_cmd(self, ops: bytes,
                            local_mem: int=0,
                            global_mem: int=0) -> bytes:
        """
        Send a direct command to the LEGO EV3
        Arguments:
        ops: holds netto data only (operations), the following fields are added:
            length: 2 bytes, little endian
            counter: 2 bytes, little endian
            type: 1 byte, DIRECT_COMMAND_REPLY or DIRECT_COMMAND_NO_REPLY
            header: 2 bytes, holds sizes of local and global memory
        Keyword Arguments:
        local_mem: size of the local memory
        global_mem: size of the global memory
        Returns:
            sync_mode is STD: reply (if global_mem > 0) or message counter
            sync_mode is ASYNC: message counter
            sync_mode is SYNC: reply of the LEGO EV3
        """
        if global_mem > 0 or self._sync_mode == const.SYNC:
            cmd_type = const._DIRECT_COMMAND_REPLY
        else:
            cmd_type = const._DIRECT_COMMAND_NO_REPLY
        self._lock.acquire()
        if self._msg_cnt < 65535:
            self._msg_cnt += 1
        else:
            self._msg_cnt = 1
        self._lock.release()
        cmd = b''.join([
            struct.pack('<hh', len(ops) + 5, self._msg_cnt),
            cmd_type,
            struct.pack('<h', local_mem * 1024 + global_mem),
            ops
        ])
        if self._verbosity >= 1:
            now = datetime.datetime.now().strftime('%H:%M:%S.%f')
            print(now + \
                    ' Sent 0x|' + \
                    ':'.join('{:02X}'.format(byte) for byte in cmd[0:2]) + '|' + \
                    ':'.join('{:02X}'.format(byte) for byte in cmd[2:4]) + '|' + \
                    ':'.join('{:02X}'.format(byte) for byte in cmd[4:5]) + '|' + \
                    ':'.join('{:02X}'.format(byte) for byte in cmd[5:7]) + '|' + \
                    ':'.join('{:02X}'.format(byte) for byte in cmd[7:]) + '|' \
            )
#         if self._protocol in [self.BLUETOOTH, self.WIFI]:
        #     self._socket.send(cmd)
        self.Send(bytes.decode(base64.b64encode(cmd)))
        # elif self._protocol is USB:
        #     # pylint: disable=no-member
        #     self._device.write(_EP_OUT, cmd, 100)
        #     # pylint: enable=no-member
        # else:
        #     raise RuntimeError('No EV3 connected')
#         return cmd
        counter = cmd[2:4]
        if  cmd[4:5] == const._DIRECT_COMMAND_NO_REPLY or self._sync_mode == const.ASYNC:
            return counter
        else:
            reply = self.wait_for_reply(counter)
            return reply

    def wait_for_reply(self, counter: bytes) -> bytes:
        """
        Ask the LEGO EV3 for a reply and wait until it is received
        Arguments:
        counter: is the message counter of the corresponding send_direct_cmd
        Returns:
        reply to the direct command
        """
        self._lock.acquire()
        reply = None  # self._get_foreign_reply(counter)
        if reply:
            self._lock.release()
            if reply[4:5] != const._DIRECT_REPLY:
                raise Exception(
                    "direct command {:02X}:{:02X} replied error".format(
                        reply[2],
                        reply[3]
                    )
                )
            return reply
        self.waitMap[counter] = None
        while True:
            # pylint: disable=no-member
#             if self._protocol in [BLUETOOTH, WIFI]:
#             reply = self._socket.recv(1024)
            while self.waitMap[counter] == None:
                time.sleep(0.0000000001)
            reply = self.waitMap[counter]
            del self.waitMap[counter]
#             else:
#                 reply = bytes(self._device.read(_EP_IN, 1024, 0))
            # pylint: enable=no-member
            len_data = struct.unpack('<H', reply[:2])[0] + 2
            reply_counter = reply[2:4]
            if self._verbosity >= 1:
                now = datetime.datetime.now().strftime('%H:%M:%S.%f')
                print(now + \
                      ' Recv 0x|' + \
                      ':'.join('{:02X}'.format(byte) for byte in reply[0:2]) + \
                      '|' + \
                      ':'.join('{:02X}'.format(byte) for byte in reply[2:4]) + \
                      '|' + \
                      ':'.join('{:02X}'.format(byte) for byte in reply[4:5]) + \
                      '|', end='')
                if len_data > 5:
                    dat = ':'.join('{:02X}'.format(byte) for byte in reply[5:len_data])
                    print(dat + '|')
                else:
                    print()
            if counter != reply_counter:
                self._put_foreign_reply(reply_counter, reply[:len_data])
            else:
                self._lock.release()
                if reply[4:5] != const._DIRECT_REPLY:
                    raise Exception(
                        "direct command {:02X}:{:02X} replied error".format(
                            reply[2],
                            reply[3]
                        )
                    )
                return reply[:len_data]
