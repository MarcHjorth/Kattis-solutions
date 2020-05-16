x, y, n = [int(q) for q in input().split()]

fizz = x
buzz = y

for _ in range(1, n + 1):
    if _ % fizz == 0 and _ % buzz == 0:
        print('FizzBuzz')
    elif _ % fizz == 0:
        print('Fizz')
    elif _ % buzz == 0:
        print('Buzz')
    else:
        print(_)

