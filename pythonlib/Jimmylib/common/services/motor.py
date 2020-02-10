
from .lego_service import LegoService
from .output_command import OutputCommand
from enum import Enum

MOTOR_MIN_SPEED = 1
MOTOR_MAX_SPEED = 100
MOTOR_POWER_BRAKE = 127
MOTOR_POWER_DRIFT = 0

MOTOR_POWER_OFFSET = 35
SERVICE_MOTOR_NAME = "Motor"


class MotorDirection(Enum):
    MOTOR_DIRECTION_DRIFTING = 0
    MOTOR_DIRECTION_LEFT = 1
    MOTOR_DIRECTION_RIGHT = 2
    MOTOR_DIRECTION_BRAKING = 3
    

class Motor(LegoService):

    def __init__(self, connect_info, io):
        super(Motor, self).__init__(connect_info, io)

#     def create_service(connect_info, io):
#         return Motor(connect_info, io)

    def get_service_name(self):
        return SERVICE_MOTOR_NAME

    def get_power(self):
        if self.most_recent_send_power == MOTOR_POWER_BRAKE or \
                self.most_recent_send_power == MOTOR_POWER_DRIFT:
            return 0
        return abs(self.most_recent_send_power)

    def is_braking(self):
        return self.most_recent_send_power == MOTOR_POWER_BRAKE

    def is_drifting(self):
        return self.most_recent_send_power == MOTOR_POWER_DRIFT

    def run(self, direction, power):
        if power == MOTOR_POWER_DRIFT:
            self.drift()
        else:
            converted_power = self.convert_unsigned_motor_power_to_signed(power, direction)
            self.send_power(converted_power)

    def brake(self):
        self.send_power(MOTOR_POWER_BRAKE)

    def drift(self):
        self.send_power(MOTOR_POWER_DRIFT)

    def send_power(self, power):
        if power == MOTOR_POWER_BRAKE or power == MOTOR_POWER_DRIFT:
            self.write_motor_power(power, 0, self.connect_info.connect_id)
        else:
            offset = 35

            self.write_motor_power(power, offset, self.connect_info.connect_id)
            
    def write_motor_power(self, power, offset, connect_id):
        is_positive = power >= 0
        power = abs(power)

        actual_power = ((100.0 - offset) / 100.0) * power + offset
        actual_result_int = round(actual_power)

        if not is_positive:
            actual_result_int = -actual_result_int

        output_command = OutputCommand.command_write_motor_power(actual_result_int, connect_id)
#         print(output_command.data)
        self.io.sendcmd(output_command.data)
        
    def convert_unsigned_motor_power_to_signed(self, power, direction):
        result_power = 0
        if power < MOTOR_MAX_SPEED:
            result_power = power
        else:
            result_power = MOTOR_MAX_SPEED

        if direction == MotorDirection.MOTOR_DIRECTION_LEFT:
            result_power = -result_power

        return result_power

