import sys

lines = sys.stdin.readlines()

values = list()

for i in lines:
    values.append(i.rstrip('\n'))

print(values)

numbersOfListsToCreate = 0

firstNumber = int(values[0])

firstRide = list()
for value in values[1:firstNumber+1]:
    firstRide.append(value)

del values[:firstNumber+1]
print(firstRide)
print(values)