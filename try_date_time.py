import time
import datetime


today_date = datetime.date.today()
conv_time = datetime.time(0, 0, 0)
date_time = datetime.datetime.combine(today_date, conv_time)
unix_date_time = date_time.strftime('%s')
print(unix_date_time)
