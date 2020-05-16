import sys

lines = sys.stdin.readlines()

values = list()

for i in lines:
    values.append(i.rstrip('\n'))

AmountOfColdDays = 0
Days = list(values[1].split(' '))

for day in Days:
    if int(day) < 0:
        AmountOfColdDays += 1

print(AmountOfColdDays)