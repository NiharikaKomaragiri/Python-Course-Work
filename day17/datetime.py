#Date and Time
from datetime import date,time,datetime,timedelta

t=date.today()
print(t)

print(t)
print(t.month)
print(t.year)
print(t.day)
print(t.weekday())#monday=0,tue=1,wed=2
print(t.isoweekday())

#Date
year,month,day=list(map(int,input("Enter the DOB :").split('-')))
print(date(year,month,day))

#Time
hour,minute,second=list(map(int,input("Enter the Time :").split(':')))
print(time(hour,minute,second))


n=datetime.now()#present time and date extarction

print(n.year)
print(n.month)
print(n.day)
print(n.hour)
print(n.minute)
print(n.second)

n = datetime.now()

print(n.strftime('%Y/%m/%d'))
print(n.strftime('%y/%m/%d'))
print(n.strftime('%y %m %d %H:%M:%S'))
print(n.strftime('%y %m %d %I:%M:%S %p'))
print(n.strftime('%a, %d %b %Y  %I:%M:%S %p'))
print(n.strftime('%A,%d %B %Y  %I:%M:%S %p'))

n=datetime.now()
d=date.today()

a7=d-timedelta(days=20)
a15=n+timedelta(minutes=15)

print(a15)


























