def tell_the_time_berlin(time_string):

    time_list = time_string.split(":")

    hours = time_list[0]
    mins = time_list[1]
    secs = time_list[2]

    row1 = int(hours/5)
    row2 = hours % 5
    row3 = int(mins/5)
    row4 = mins % 5
    row_big_round_light = (mins % 2 == 0)

    output_string = ''

    return output_string


