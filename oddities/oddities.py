import sys

inputData = sys.stdin.readlines()

inputDataList = list()
for value in inputData:
    inputDataList.append(int(value.rstrip('\n')))

del inputDataList[0]

for number in inputDataList:
    if number % 2 == 0:
        print(number, ' is even')
    else:
        print(number, ' is odd')
