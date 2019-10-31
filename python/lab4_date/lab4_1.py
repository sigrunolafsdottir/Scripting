from datetime import date
from datetime import datetime


xmas = date(2019, 12, 24)
now = date.today()
delta = xmas - now
print (delta.days)


xmas2 = datetime(2019, 12, 24, 23, 0, 0)
now2 = datetime.now()
delta2 = xmas2 - now2
print (delta2.days)