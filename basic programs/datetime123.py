'''import datetime
import time
print(time.time())
print(time.asctime())
sadiya=datetime.datetime.now()
print(sadiya)
print("year:",sadiya.year)

import calendar
s=calendar.prcal(3023)
s2=calendar.month(2023,4)
s1=calendar.isleap(2005)
print(s1)'''

import datetime
x=datetime.datetime.now()
from datetime import timedelta
print(x+timedelta(days=-89))

import time
from datetime import datetime
import pytz
time1=pytz.timezone('America/Aruba')
print("current time is:",datetime.now(time1))
