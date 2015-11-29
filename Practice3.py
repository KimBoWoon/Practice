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

# for i in range(int(input())):
#     x = int(input())
#     n = x
#     for i in range(x):
#         if (i < x / 2):
#             n -= 1
#         else:
#             n += 1
#         for k in range(x):
#             if (k < n):
#                 print(' ', end='')
#             elif (k == n or k == x - 1):
#                 print('*', end='')
#             else:
#                 print('+', end='')
#         print()

for t in range(int(input())):
    data = input()

    size = len(data)
    sum = 0
    checkSum = 0

    for i in range(1, size):
        if i % 2 == 0:
            temp = int(data[i - 1]) * 2
            if temp > 10:
                sum += temp - 9
            else:
                sum += temp
        else:
            sum += int(data[i - 1])

    checkSum = sum + int(data[-1])

    if data[0] == '3' and size == 15 and checkSum % 10 == 0:
        print(1)
    elif data[0] == '3' and size == 14 and checkSum % 10 == 0:
        print(1)
    elif data[0] == '6' and size == 16 and checkSum % 10 == 0:
        print(1)
    elif data[0] == '5' and size == 16 and checkSum % 10 == 0:
        print(1)
    elif data[0] == '4' and (size == 13 or size == 16) and checkSum % 10 == 0:
        print(1)
    else:
        print(0)