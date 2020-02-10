
from .lego_service import LegoService
from .data_format import DataFormat
from .input_format import InputFormat, InputFormatUnit
from .input_command import InputCommand
from enum import Enum

SERVICE_MOTION_SENSOR_NAME = "Motion Sensor"
MAX_DISTANCE = 100
MIN_DISTANCE = 0

UUID_CUSTOM_BASE = "1212-EFDE-1523-785FEABCD123"
UUID_STANDARD_BASE = "0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_INPUT_VALUE_UUID = "0x1560"
CHARACTERISTIC_INPUT_FORMAT_UUID = "0x1561"
CHARACTERISTIC_INPUT_COMMAND_UUID = "0x1563"
CHARACTERISTIC_OUTPUT_COMMAND_UUID = "0x1565"


class MotionSensorMode(Enum):
    MOTION_SENSOR_MODE_DETECT = 0
    MOTION_SENSOR_MODE_COUNT = 1
    MOTION_SENSOR_MODE_UNKNOWN = 2


class MotionSensor(LegoService):

    def __init__(self, connect_info, io):
        super(MotionSensor, self).__init__(connect_info, io)
        self.add_valid_data_formats()
        self.write_input_format(self.get_default_input_format(), connect_info.connect_id)
        
        # 发送通知
        txt = '{"jsonrpc":"2.0","method":"startNotifications","params":{"serviceId":"00004f0e-1212-efde-1523-785feabcd123","characteristicId":"00001560-1212-efde-1523-785feabcd123"},"id":6}'
        self.io.sendtxt(txt)

    def create_service(connect_info, io):
        return MotionSensor(connect_info, io)

    def get_service_name(self):
        return SERVICE_MOTION_SENSOR_NAME

    def get_default_input_format(self):
        return InputFormat.input_format(self.connect_info.connect_id, self.connect_info.type_id,
                                        0, 1, InputFormatUnit.INPUT_FORMAT_UNIT_PERCENTAGE, True)

    def add_valid_data_formats(self):
        self.add_valid_data_format(DataFormat.create("Detect", MotionSensorMode.MOTION_SENSOR_MODE_DETECT.value,
                                   InputFormatUnit.INPUT_FORMAT_UNIT_RAW.value, 1, 1))
        self.add_valid_data_format(DataFormat.create("Detect", MotionSensorMode.MOTION_SENSOR_MODE_DETECT.value,
                                   InputFormatUnit.INPUT_FORMAT_UNIT_PERCENTAGE.value, 1, 1))
        self.add_valid_data_format(DataFormat.create("Detect", MotionSensorMode.MOTION_SENSOR_MODE_DETECT.value,
                                   InputFormatUnit.INPUT_FORMAT_UNIT_SI.value, 4, 1))
        self.add_valid_data_format(DataFormat.create("Count", MotionSensorMode.MOTION_SENSOR_MODE_COUNT.value,
                                   InputFormatUnit.INPUT_FORMAT_UNIT_RAW.value, 4, 1))
        self.add_valid_data_format(DataFormat.create("Count", MotionSensorMode.MOTION_SENSOR_MODE_COUNT.value,
                                   InputFormatUnit.INPUT_FORMAT_UNIT_PERCENTAGE.value, 1, 1))
        self.add_valid_data_format(DataFormat.create("Count", MotionSensorMode.MOTION_SENSOR_MODE_COUNT.value,
                                   InputFormatUnit.INPUT_FORMAT_UNIT_SI.value, 4, 1))

    def get_distance(self):
        
#         txt ='{"jsonrpc":"2.0","method":"write","params":{"serviceId":"00004f0e-1212-efde-1523-785feabcd123","characteristicId":"00001565-1212-efde-1523-785feabcd123","message":"BQM=","encoding":"base64"},"id":11}'
#         self.io.sendtxt(txt)
#         txt = '{"jsonrpc":"2.0","method":"write","params":{"serviceId":"00004f0e-1212-efde-1523-785feabcd123","characteristicId":"00001565-1212-efde-1523-785feabcd123","message":"AgEBAA==","encoding":"base64"},"id":10}'
#         self.io.sendtxt(txt)
        if self.get_motion_sensor_mode() != MotionSensorMode.MOTION_SENSOR_MODE_DETECT:
            print("Cannot return object distance. Motion Sensor is not set to Detect Mode.")
            return None
        else:
            while True:
                dt = self.read_value_for_connect_id(self.connect_info.connect_id)
                if len(dt)>0:
                    break
            number = self.get_number_from_value_data(dt)
            if number is not None:
                return number
            else:
                return MAX_DISTANCE
#         return self.read_input_value()

    def read_value_for_connect_id(self, connect_id):
        input_command = InputCommand.command_read_value_for_connect_id(connect_id)
        self.write_input_command(input_command.data)
        value = self.read_input_value()
        return value

    def uuid_with_prefix_custom_base(self, prefix):
        padding = self.add_leading_zeroes(prefix)
        return "{}-{}".format(padding, UUID_CUSTOM_BASE)

    def add_leading_zeroes(self, prefix):
        hex_prefix = "0x"
        if prefix[0:2] == hex_prefix:
            prefix = prefix[2:]
        return ("00000000" + prefix)[len(prefix):]

    def write_input_format(self, input_format, connect_id):
        input_command = InputCommand.command_write_input_format(input_format, connect_id)
        self.write_input_command(input_command.data)
        
    def write_input_command(self, command):
        char_uuid = self.uuid_with_prefix_custom_base(CHARACTERISTIC_INPUT_COMMAND_UUID)
        self.io.sendcmd2(char_uuid, command)
    
    def read_input_value(self):
        data = self.io.getCurrentmsg(self.connect_info.connect_id)
        return data[2:]
    
    def get_count(self):
        if self.get_motion_sensor_mode() != MotionSensorMode.MOTION_SENSOR_MODE_COUNT:
            print("Cannot return the count. Motion Sensor is not set to Count Mode")
            return None
        else:
            number = self.get_number_from_value_data(self.io.read_value_for_connect_id(self.connect_info.connect_id))
            if number is not None:
                return int(number)
            else:
                return None

    def get_motion_sensor_mode(self):
        return MotionSensorMode(self.get_input_format_mode())

    def set_motion_sensor_mode(self, motion_sensor_mode):
        self.update_current_input_format_with_new_mode(motion_sensor_mode.value)

