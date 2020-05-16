import sys
from itertools import chain

lines = sys.stdin.readlines()
newList = list(chain.from_iterable(el.split() for el in lines))
newList.remove(newList[0])

groupedList = list(zip(*[iter(newList)]*3))

for _ in groupedList:
    if int(_[1]) - int(_[0]) < int(_[2]):
        print('do not advertise')
    elif int(_[1]) - int(_[0]) > int(_[2]):
        print('advertise')
    else:
        print('does not matter')
