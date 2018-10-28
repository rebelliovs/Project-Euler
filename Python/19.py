# Importing the 'calendar' library so we can easily get the day of the week
import calendar

# Initializing the number of Sundays to 0
sundays = 0

# Iterating through the loops from 1901 to 2000 inclusive
# and for months from 1 to 12;
for y in range(1901,2001):
	for m in range(1, 13):
		if calendar.weekday(y,m,1) == calendar.SUNDAY:
			sundays += 1

print("Between 1901 and 2000 inclusive, there have been",sundays,"Sundays on the first day of the month")

# Problem 19 on Project Euler
# https://projecteuler.net/problem=19