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
    no_of_lights = int(int(seconds) % 2 == 0)
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
    row_list[:number_to_fill] = [filler_character] * number_to_fill
    return "".join(row_list)
    
    
    
