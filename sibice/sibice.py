# import math
# import sys
#
# line = [int(x) for x in input().split()]
# # print('First line: ', line)
#
# calcMatchbox = math.sqrt((line[1] * line[1]) + (line[2] * line[2]))
# # print('Matchbox: ', calcMatchbox)
#
# lines = sys.stdin.readlines()
# for value in lines:
#     if int(value) <= int(calcMatchbox):
#         print('DA')
#     else:
#         print('NE')

import math

n, w, h = [int(q) for q in input().split()]
hyp = math.sqrt(w*w + h*h)

for _ in range(n):
    if int(input()) <= hyp:
        print('DA')
    else:
        print('NE')
