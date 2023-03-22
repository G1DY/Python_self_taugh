''' CASE: Study to display current time in Greenwinch Meridian Time
in the format hour:minute:second'''
import time

#get current time
currentTime = time.time()

#obtain the total seconds since midnight jan 1 1970(unix epoch)
totalSeconds = int(currentTime)

#get current seconds
currentSeconds = totalSeconds % 60

#get total minutes
totalMinutes = totalSeconds // 60

#get current minutes
currentMinutes = totalMinutes % 60

#get total hours
totalHours = totalMinutes // 60

#get current hour
currentHour = totalHours % 24

#Display results
print("Current Time is", currentHour, ":",currentMinutes, ":",currentSeconds, "GMT")
