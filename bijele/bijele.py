k, q, r, b, kn, p = [int(q) for q in input().split()]

kingNeeded = 1
queenNeeded = 1
rooksNeeded = 2
bishopsNeeded = 2
knightsNeeded = 2
pawnsNeeded = 8

listOfPiecesNeeded = list()

if k is 0:
    listOfPiecesNeeded.append(1)
else:
    listOfPiecesNeeded.append(kingNeeded - k)

if q is 0:
    listOfPiecesNeeded.append(1)
else:
    listOfPiecesNeeded.append(queenNeeded - q)

if r is 0:
    listOfPiecesNeeded.append(2)
else:
    listOfPiecesNeeded.append(rooksNeeded - r)

if b is 0:
    listOfPiecesNeeded.append(2)
else:
    listOfPiecesNeeded.append(bishopsNeeded - b)

if kn is 0:
    listOfPiecesNeeded.append(2)
else:
    listOfPiecesNeeded.append(knightsNeeded - kn)

if p is 0:
    listOfPiecesNeeded.append(8)
else:
    listOfPiecesNeeded.append(pawnsNeeded - p)

# print(listOfPiecesNeeded)

answer = str()

for _ in listOfPiecesNeeded:
    answer += str(_) + ' '

print(answer)