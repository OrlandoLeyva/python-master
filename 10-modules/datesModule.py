# native module that allows you to work with dates
import datetime 

# provides you with a lot of methods for working with dates
date = datetime.date.today() # return the current date: YYYYY/MM/DD

fullDate = datetime.datetime.now() # return the whole date including hours, minutes, seconds and milliseconds

fullDate.day # getting the day form the date.

fullDate.minute
fullDate.microsecond
fullDate.hour
fullDate.month
fullDate.year
fullDate.day

customDate = fullDate.strftime('%d--%m--%Y') 

print(customDate)

# %d = day
# %m = month
# %Y = year

# %H = hour
# %M = minutes
# %S = seconds