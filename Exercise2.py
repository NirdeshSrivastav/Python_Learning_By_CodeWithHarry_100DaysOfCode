import time as d

timestamp = d.strftime('%H:%M:%S')

print(timestamp)

if timestamp <= '12:00:00':
    print("Good Morning")
elif '16:00:00' >= timestamp > '12:00:00':
    print("Good Afternoon")
elif timestamp <= '20:00:00' and timestamp > '16:00:00':
    print("Good Evening")
else:
    print("Good Night")