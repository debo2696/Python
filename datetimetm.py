import datetime                    
import time                
tod=datetime.date.today() 
now=datetime.datetime.now()
com=datetime.datetime.combine(now,datetime.datetime.min.time())
a=datetime.date(1996,12,26)
b=datetime.date(2018,4,12)
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Current year: ", datetime.date.today().year)
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))
print("5days bfor the current date:",datetime.datetime.now()-datetime.timedelta(5))
print(datetime.datetime.fromtimestamp(int("1254105681")).strftime('%Y-%m-%d %H:%M:%S'))
print("yesterday's date:",tod - datetime.timedelta(days=1))
print("Combined with date:",datetime.datetime.combine(tod,datetime.datetime.min.time()))
print("Add 5secs with curr time:",com+datetime.timedelta(1,2,3,4,5,6,7))
print("Breathing for these many days:",datetime.date.today()-a)
print(time.ctime())
'''from datetime import date,datetime,timedelta
import time

for i in range (3):
	print(datetime.now())
	time.sleep(2)

print("Year:",date.today().strftime("%Y"))  #creates formatted date time
print("Month:",date.today().strftime("%M"))
print("Week:",date.today().strftime("%W"))
print("day of Week:",date.today().strftime("%A"))
dt_obj = datetime.strptime('Jul 1 2014 2:54pm', "%b %d %Y %I:%M%p") #converts a string to date time
print(dt_obj)
print(datetime.now().time())
print("5 days bfor curr.date:",datetime.now()-timedelta(5))
print("unix time stamp:",datetime.fromtimestamp(int("1254105681")).strftime('%Y-%m-%d %H:%M:%S'))
help(timedelta)'''