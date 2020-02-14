def tell_the_time_berlin(time_string):

    time_list = time_string.split(":")

    hours = time_list[0]
    mins = time_list[1]
    secs = time_list[2]
    
    row1 = get_row_1(secs)
    row2 = get_row_2(hours)
    row3 = get_row_3(hours)
    row4 = get_row_4(mins)
    row5 = get_row_5(mins)
    
    list_of_rows =[row1, row2, row3, row4, row5]
    
    output_string = "\n".join(list_of_rows)

    return output_string


def get_row_1(seconds):
    no_of_lights = int(seconds) % 2 == 0
    return create_row_string(1, no_of_lights, 'Y')

def get_row_2(hours):
    no_of_lights = int(int(hours)/5)
    return create_row_string(4, no_of_lights, 'R')

def get_row_3(hours):
    no_of_lights = int(int(hours)) % 5
    return create_row_string(4, no_of_lights, 'R')

def get_row_4(minutes):
    no_of_lights = int(int(minutes)/5)
    return create_row_string(11, no_of_lights, 'Y')

def get_row_5(minutes):
    no_of_lights = int(int(minutes)) % 5
    return create_row_string(4, no_of_lights, 'Y')

def create_row_string(length, number_to_fill, filler_character):
    row_list = ["O"] * length
    if number_to_fill > 0:
        row_list[:number_to_fill] = [filler_character] * number_to_fill
    return "".join(row_list)
    
    
    
class BerlinClock:
    self __init__(self, time_string):
        time_list = time_string.split(":")
        self.hour = Hour(time_list[0])
        self.minutes = Minutes(time_list[1])
        self.seconds = Seconds(time_list[2])
        
class TimeComponent:
    def __init__(self, count):
        self.count = count
    
    @classmethod    
    def get_list_of_row_strings(self):
        pass
    
    @classmethod
    def create_row_string(self, length, number_to_fill, filler_character):
        row_list = ["O"] * length
        if number_to_fill > 0:
            row_list[:number_to_fill] = [filler_character] * number_to_fill
        return "".join(row_list)
                
class Hour(TimeComponent):
    def __init__(self, count):
        super().__init__(self, count)
    
class Minutes(TimeComponent):
    def __init__(self, count):
        super().__init__(self, count)

class Seconds(TimeComponent):
    def __init__(self, count):
        super().__init__(self, count)