
HEADER_SIZE = 3

COMMAND_ID_INPUT_VALUE = 0
COMMAND_ID_INPUT_FORMAT = 1

COMMAND_TYPE_READ = 1
COMMAND_TYPE_WRITE = 2


class InputCommand:
    
    def __init__(self, command_id, command_type, connect_id, payload_data):
        data = bytearray(HEADER_SIZE + len(payload_data))
        data[0] = command_id
        data[1] = command_type
        data[2] = connect_id
        
        index = HEADER_SIZE
        for byte in payload_data:
            data[index] = byte
            index += 1

        self.data = data

    def command_write_input_format(f, connect_id):
        return InputCommand(COMMAND_ID_INPUT_FORMAT, COMMAND_TYPE_WRITE, connect_id, f.input_format_to_byte_array())
        
    def command_read_input_format_for_connect_id(connect_id):
        return InputCommand(COMMAND_ID_INPUT_FORMAT, COMMAND_TYPE_READ, connect_id, bytearray(0))

    def command_read_value_for_connect_id(connect_id):
        return InputCommand(COMMAND_ID_INPUT_VALUE, COMMAND_TYPE_READ, connect_id, bytearray(0))
