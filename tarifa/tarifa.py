import sys

lines = sys.stdin.readlines()

values = list()

for i in lines:
    values.append(i.rstrip('\n'))

amountOfMegabytes = int(values[0])

months = list()

for value in values[2:]:
    months.append(value)

amountOfMegabytesLeft = int(values[0])

for value in months:
    y = amountOfMegabytes - int(value)
    amountOfMegabytesLeft += y

print(amountOfMegabytesLeft)
