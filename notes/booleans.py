# JS, 1st, Booleans Notes

import time
import datetime as date

while True:
    current_time = time.time()
    readable_time = time.ctime(current_time)
    current_time_using_datetime = date.datetime.now()
    hour = current_time_using_datetime.strftime("%H")
    minutes = current_time_using_datetime.strftime("%M")
    days = current_time_using_datetime.strftime("%d")
    month = current_time_using_datetime.strftime("%B")
    month_num = current_time_using_datetime.strftime("%m")
    year = current_time_using_datetime.strftime("%Y")
    seconds = current_time_using_datetime.strftime("%S")
    print(f"Current time in seconds since January 1, 1970 (epoch): {current_time}\nReadable as {readable_time}\n  Date time: {current_time_using_datetime}")
    print(f"The hour is saved as an integer: {isinstance(hour, int)}")
    print(f"The hour is saved as an integer: {isinstance(hour, float)}")
    print(f"The hour is saved as an string: {not isinstance(hour, str)}")
    print(bool('a'))
    print(hour.isalpha())
    time.sleep(.1)
    print("\033c", end="")