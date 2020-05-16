import sys

input_data = sys.stdin.readline().split(' ')

hour_minutes = list()

for value in input_data:
    hour_minutes.append(int(value.rstrip('\n')))

newMinutes = int()
newHour = int(hour_minutes[0])

if int(hour_minutes[1]) < 45:
    difference = 45 - int(hour_minutes[1])
    newMinutes = 60 - difference
    if hour_minutes[0] is 0:
        newHour = 23
    else:
        newHour -= 1
else:
    newMinutes = int(hour_minutes[1]) - 45

print(newHour, newMinutes)
