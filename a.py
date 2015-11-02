__author__ = '보운'

T = int(input())
n = 0
for t in range(T):
    size = int(input())
    for i in range(size):
        if i < size / 2:
            n += 1
        else:
            n -= 1
        print(" " * (size - n), end="")
        for j in range(n - 1):
            if (j == 0 or j == n):
                print("*", end="")
            else:
                print("+", end="")
        print("*")
