a, b = [int(q) for q in input().split()]

a_str = str(a)[::-1]
b_str = str(b)[::-1]

if int(a_str) > int(b_str):
    print(a_str)
else:
    print(b_str)
