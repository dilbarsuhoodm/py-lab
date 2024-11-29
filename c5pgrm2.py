import time
from datetime import datetime

print("Current date and time:", datetime.now())
print("Current Year:", datetime.now().year)
print("Month of the year:", datetime.now().month)
print("Week number of the year:", datetime.now().isocalendar()[1])
print("Day of year:", datetime.now().timetuple().tm_yday)
print("Day of the month:", datetime.now().day)
print("Day of week:", datetime.now().strftime('%A'))
print("Day of the week as number:", datetime.now().weekday() + 1)
