import datetime

def add_to_time(time_obj, timedelta_obj):
    datetime_obj = datetime.datetime.combine(datetime.date.today(), time_obj)
    datetime_obj += timedelta_obj
    return datetime_obj.time()