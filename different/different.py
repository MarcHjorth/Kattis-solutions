import sys

lines = sys.stdin.readlines()

values = list()

for i in lines:
    values.append(i.rstrip('\n'))

splittedList = list()

for _ in values:
    x = _.split(' ')
    splittedList.append(x)


for _ in splittedList:
    if int(_[0]) < int(_[1]):
        print(int(_[1])-int(_[0]))
    else:
        print(int(_[0]) - int(_[1]))
