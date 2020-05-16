import sys

x = sys.stdin.readline()

y = x.split('-')

shortenedName = str()
for _ in y:
    shortenedName += _[0]

print(shortenedName)