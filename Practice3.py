__author__ = '보운'

# x = int(input())
# x = 9
# for i in range(x):
#     if (i < x / 2):
#         n = i + 1
#     else:
#         n = x - i
#     for j in range(n):
#         if (j == 0 or j == n - 1):
#             print('*', end='')
#         else:
#             print('+', end='')
#     print()

for i in range(int(input())):
    x = int(input())
    n = x
    for i in range(x):
        if (i < x / 2):
            n -= 1
        else:
            n += 1
        for k in range(x):
            if (k < n):
                print(' ', end='')
            elif (k == n or k == x - 1):
                print('*', end='')
            else:
                print('+', end='')
        print()
