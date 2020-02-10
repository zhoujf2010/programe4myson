
from .input_format import InputFormatUnit
from . import byte_utils


class LegoService(object):

    def __init__(self, connect_info, io):
        assert connect_info is not None, "Cannot instantiate service with null ConnectInfo"
        assert io is not None, "Cannot instantiate service with null IO"

        self.connect_info = connect_info
        self.io = io
        self.valid_data_formats = set()
        self.input_format = self.get_default_input_format()
        self.value_data = None

    def create_service(connect_info, io):
        return LegoService(connect_info, io)

    def verify_data(self, *args):
        if len(args) == 1:
            data = args[0]
            if data is not None and len(self.valid_data_formats) != 0:
                d_format = self.data_format_for_input_format(self.input_format)
                if d_format is None:
                    raise Exception("Did not find a valid input data format")

                self.verify_data(data, d_format)
                
        elif len(args) == 2:
            data = args[0]
            d_format = args[1]
            if len(data) != (d_format.dataset_size * d_format.dataset_count):
                raise Exception("Package sizes don't add up. Something is wrong")

    def data_format_for_input_format(self, i_format):
        for d_format in self.valid_data_formats:
            if d_format.mode == i_format.mode and d_format.unit == i_format.unit:
                return d_format
        return None

    def get_service_name(self):
        return "Undefined"

    def get_default_input_format(self):
        return None

    def update_input_format(self, new_format):
        self.io.write_input_format(new_format, self.connect_info.connect_id)
        self.input_format = new_format

    def get_input_format_mode(self):
        if self.input_format is not None:
            return self.input_format.mode
        elif self.get_default_input_format() is not None:
            return self.get_default_input_format().mode
        return 0

    def update_current_input_format_with_new_mode(self, new_mode):
        if self.input_format is not None:
            self.update_input_format(self.input_format.input_format_by_setting_mode(new_mode))
        elif self.get_default_input_format() is not None:
            self.update_input_format(self.get_default_input_format().input_format_by_setting_mode(new_mode))
        else:
            print("Couldn't update input format")      

    def add_valid_data_format(self, d_format):
        assert d_format is not None, "DataFormat cannot be None"
        self.valid_data_formats.add(d_format)

    def remove_valid_data_format(self, d_format):
        assert d_format is not None, "DataFormat cannot be None"
        if len(self.valid_data_formats == 0):
            return
        self.valid_data_formats.remove(d_format)

    # 0 or 1 argument
    def get_number_from_value_data(self, *args):
        if len(args) == 0:
            return self.get_number_from_value_data(self.value_data)
        else:  # len(args) == 1
            data = args[0]
            values_as_numbers = self.get_numbers_from_value_data_set(data)
            if values_as_numbers is None:
                return None

            if len(values_as_numbers) != 1:
                return None
            
            return values_as_numbers[0]

    # 0 or 1 argument
    def get_numbers_from_value_data_set(self, *args):
        if len(args) == 0:
            return self.get_numbers_from_value_data_set(self.value_data)
        else:  # len(args) == 1
            data_set = args[0]
            if data_set is None:
                return None

            d_format = self.data_format_for_input_format(self.input_format)
            if d_format is None:
                print("d_format was None")
                return None

            try:
                self.verify_data(data_set, d_format)
                result_array = []

                current_index = 0
                for i in range(0, d_format.dataset_count):
                    current_index = i * d_format.dataset_size
                    data_set_bytes = bytearray(data_set[current_index: current_index + d_format.dataset_size])
                    if d_format.unit ==  0 or  d_format.unit ==1 :#InputFormatUnit.INPUT_FORMAT_UNIT_RAW or \
#                             d_format.unit == InputFormatUnit.INPUT_FORMAT_UNIT_PERCENTAGE:

                        result_array.append(self.get_integer_from_data(data_set_bytes))
                    else:
                        result_array.append(self.get_float_from_data(data_set_bytes))
                return result_array

            except:
                return None

    def get_float_from_data(self, data):
        if len(data) > 4:
            return 0
        return byte_utils.get_float(data)
            
    def get_integer_from_data(self, data):
        if len(data) == 1:
            return data[0]
        elif len(data) == 2:
            return byte_utils.get_short(data)
        elif len(data) == 4:
            return byte_utils.get_int(data)
        else:
            return 0        

    def __eq__(self, obj):
        if obj is None:
            return False
        elif self.connect_info != obj.connect_info:
            return False
        else:
            return True

    def __ne__(self, obj):
        return not self.__eq__(obj)

    def __hash__(self):
        return hash(str(self))

    
    
        
