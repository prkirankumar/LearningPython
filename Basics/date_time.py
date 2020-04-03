import datetime
import time

print(datetime.timezone)
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
print(datetime.tzinfo)

print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime.utcfromtimestamp(time.time()))
print(time.time())

d=datetime.date.today()
print(d.day)
print(d.month)
print(d.year)
print(d.weekday())
print(d.timetuple())
print(d.isocalendar())

print(d.__str__())
print(d.ctime())