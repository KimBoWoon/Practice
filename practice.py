__author__ = 'user'

i = int(input())
for a in range(i):
    x = int(input())
    for row in range(x):
        for col in range(x):
            if (row == 0) or (row == x - 1) or (col == 0) or (col == x - 1):
                print('*', end='')
            else:
                print('+', end='')
        print()