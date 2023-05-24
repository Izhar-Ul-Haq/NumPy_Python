import calendar
import datetime

year = datetime.datetime.now().year

thisCalendar = calendar.calendar(year)
thisMonth = datetime.datetime.now().month



print(thisCalendar)
print(calendar.calendar(year, thisMonth))