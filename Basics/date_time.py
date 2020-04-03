'''
The Epoch is the point in time in Python from which time is measured. It is labelled 12:00AM, Jan 1, 1970. It is the beginning of an era.

'''
import os
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


os.system("cls")
print("----- calendar -----")
print(calendar.Calendar(firstweekday=0))

c=calendar.Calendar(firstweekday=1)
for i in c.iterweekdays():
    print(i)

c=calendar.Calendar(firstweekday=0)
for i in c.itermonthdates(2019,12):
    print(i)

for i in c.itermonthdays(2018,12):
    print(i)

for i in c.itermonthdays2(2018,12):
    print(i)

for i in c.itermonthdays3(2018,12):
    print(i)

for i in c.itermonthdays4(2018,12):
    print(i)

for i in c.monthdatescalendar(2018,12):
    print(i)

for i in c.monthdays2calendar(2018,12):
    print(i)

for i in c.monthdayscalendar(2018,12):
        print(i)

for i in c.yeardatescalendar(2018,2):
    print(i)

for i in c.yeardays2calendar(2018,2):
    print(i)

for i in c.yeardayscalendar(2018,2):
    print(i)

t=calendar.TextCalendar(0)
print(t.formatmonth(2018,12))

print(t.prmonth(2018,12))

print(t.formatyear(2018,5)) #sets w=5 and m is 3 by default
print(t.formatyear(2018,m=5))

print(t.pryear(2018,m=5))

# html calendar
os.system("cls")

h=calendar.HTMLCalendar()
print(h.formatmonth(2018,12)) # formatmonth(theyear,themonth,withyear=True)

print(h.formatyear(2018,5)) # year width

print(h.formatyearpage(2018,css=None)) # formatyearpage(theyear,width=3,css=’calendar.css’,encoding=None)

t.setfirstweekday(calendar.SUNDAY)
print(t.formatyear(2018,5))
print(t.firstweekday)
print(calendar.isleap(2020))
print(calendar.leapdays(1990,2020))
print(calendar.weekday(2018,12,31))
print(calendar.weekheader(1))
print(calendar.weekheader(2))
print(calendar.weekheader(3))

print(calendar.monthrange(2018,12))

for i in calendar.monthcalendar(2018,12):
    print(i)

print(calendar.prmonth(2018,12))
print(calendar.month(2018,12))
print(calendar.prcal(2018))
print(calendar.calendar(2020))