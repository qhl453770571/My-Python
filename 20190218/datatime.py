
from datetime import datetime,timedelta

t=datetime.now()
print(t)

# print(t.month)
# print(t.day)
# print(t.year)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)
#
# t1=datetime(2018,10,1)
#
# print(t1.year)
# print(t1.microsecond)

days=timedelta(2)

t=t+days

print(t)

print(t-days)

print('hello'[4])


