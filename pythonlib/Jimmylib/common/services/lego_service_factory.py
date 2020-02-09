
from .motor import Motor
from .motion_sensor import MotionSensor
from .tilt_sensor import TiltSensor
# from wedo.services.piezo_tone_player import PiezoTonePlayer 
# from wedo.services.motor import Motor
# from wedo.services.current_sensor import CurrentSensor
# from wedo.services.voltage_sensor import VoltageSensor
# from wedo.services.rgb_light import RGBLight
from .connect_info import ConnectInfo, IOType
# from wedo.services.generic_service import GenericService


class LegoServiceFactory:

    def create(self,connect_info, io):
        if io == None or connect_info == None:
            print("Cannot instantiate service")
            return None

        result = None
        type_enum = connect_info.get_type_enum()

        if type_enum == IOType.IO_TYPE_MOTOR:
            result = Motor(connect_info, io)
        elif type_enum == IOType.IO_TYPE_MOTION_SENSOR:
            result = MotionSensor.create_service(connect_info, io)
        elif type_enum == IOType.IO_TYPE_TILT_SENSOR:
            result = TiltSensor.create_service(connect_info, io)
            
            # Motor.create_service(connect_info, io)
#         elif type_enum == IOType.IO_TYPE_GENERIC:
#             result = GenericService.create_service(connect_info, io)
#         elif type_enum == IOType.IO_TYPE_PIEZO_TONE_PLAYER:
#             result = PiezoTonePlayer.create_service(connect_info, io)
#         elif type_enum == IOType.IO_TYPE_CURRENT:
#             result = CurrentSensor.create_service(connect_info, io)
#         elif type_enum == IOType.IO_TYPE_VOLTAGE:
#             result = VoltageSensor.create_service(connect_info, io)
#         elif type_enum == IOType.IO_TYPE_RGB_LIGHT:
#             result = RGBLight.create_service(connect_info, io)
#         else:
#             result = GenericService.create_service(connect_info, io)

        return result
    


