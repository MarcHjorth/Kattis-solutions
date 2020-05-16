import sys

lines = sys.stdin.readlines()

newList = list()

for i in lines:
    newList.append(i.rstrip('\n'))

AbleToSay = len(newList[0])
HasToSay = len(newList[1])

if AbleToSay >= HasToSay:
    print('go')
else:
    print('no')
