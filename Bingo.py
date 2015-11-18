__author__ = '보운'

def func():
    numbers = input().split()
    cnt = 0

    for t in range(len(numbers)):
        for x in range(5):
            for y in range(5):
                if matrix[x][y] == int(numbers[t]):
                    matrix[x][y] = 0

        for _x in range(5):
            for _y in range(5):
                if matrix[_x][_y] == 0:
                    cnt += 1
            if cnt == 5:
                return t + 1
            else:
                cnt = 0

        for _x in range(5):
            for _y in range(5):
                if matrix[_y][_x] == 0:
                    cnt += 1
            if cnt == 5:
                return t + 1
            else:
                cnt = 0

        for _x in range(5):
            if matrix[_x][_x] == 0:
                cnt += 1
            if cnt == 5:
                return t + 1
        cnt = 0

        for _x in range(5):
            for _y in range(5):
                if _x + _y == 4:
                    if matrix[_x][_y] == 0:
                        cnt += 1
            if cnt == 5:
                return t + 1
        cnt = 0

        if matrix[0][0] == 0:
            cnt += 1
        if matrix[0][4] == 0:
            cnt += 1
        if matrix[4][0] == 0:
            cnt += 1
        if matrix[4][4] == 0:
            cnt += 1

        if cnt == 4:
            return t + 1
        cnt = 0


T = int(input())
matrix = [[0 for col in range(5)] for row in range(5)]
for t in range(T):
    for x in range(5):
        temp = input().split()
        for y in range(5):
            matrix[x][y] = int(temp[y])

    print(func())
