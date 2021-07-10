from datetime import datetime, date, timedelta

# HW
dt = date.today()
print(f"Yesterday - {dt - timedelta(days=1)}, "
      f"Today - {dt}, 30-days ago - {dt - timedelta(days=30)}")
dt_string = '01/01/25 12:10:03.234567'
date_dt = datetime.strptime(dt_string, '%m/%d/%y %H:%M:%S.%f')
print(date_dt)
