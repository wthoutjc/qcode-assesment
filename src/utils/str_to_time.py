import datetime

def str_to_time(time_str):
    return datetime.datetime.strptime(time_str, '%H:%M:%S').time()