from collections import Counter

line = [int(x) for x in input().split()]

n = int(line[0])
m = int(line[1])
# print('n: ', n)
# print('m: ', m)

Dice_list = list()

for face in range(1, n + 1):
    for other_face in range(1, m + 1):
        x = face + other_face
        Dice_list.append(x)
        Dice_list.append(x)

# print('Roll: ', Dice_list)

sortedList = Counter(Dice_list)
# print('Most common: ', sortedList.most_common())

# print(sortedList.most_common()[0])

MostProbableRoll = list()

HighestPossibility = sortedList.most_common()[0][1]
# print('Highest possibility: ', HighestPossibility)

for value in sortedList.most_common():
    if value[1] == HighestPossibility:
        MostProbableRoll.append(value)

# print(MostProbableRoll)

Result = list()

for number in MostProbableRoll:
    print(number[0])