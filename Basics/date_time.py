'''
The Epoch is the point in time in Python from which time is measured. It is labelled 12:00AM, Jan 1, 1970. It is the beginning of an era.

'''
import datetime
import time
import calendar

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

time.sleep(2) # sleeps for 2 seconds

print(time.strftime("%b",time.localtime()))
print(time.strptime("31 Dec 1995","%d %b %Y"))


print(calendar.month(2018,1))
print(calendar.month(2017,12,3,2))
print(calendar.calendar(2018))
print(calendar.monthcalendar(2017,12))
print(calendar.monthrange(2017,12)) # (4,31) 4 is friday 31 days current month

print(calendar.prcal(2020)) # print calender for 2020
print(calendar.prmonth(2020,4)) # for month
print(calendar.weekday(2020,4,5))

print(calendar.timegm(time.localtime()))
