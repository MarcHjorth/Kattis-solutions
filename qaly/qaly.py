import sys
from itertools import chain

lines = sys.stdin.readlines()

newList = list(chain.from_iterable(el.split() for el in lines))
newList.remove(newList[0])

NewNewlist = list(zip(*[iter(newList)]*2))

qalyTotal = 0.000

for _ in NewNewlist:
    qalyTotal += float(_[0]) * float(_[1])

print('%.3f' % qalyTotal)
