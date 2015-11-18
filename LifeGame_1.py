__author__ = '보운'

for t in range(int(input())):
    size, time = input().split()
    size = int(size)
    time = int(time)

    cell = input().split()
    result = [0 for i in range(size)]
    cell = [int(i) for i in cell]

    for i in range(time):
        for x in range(size):
            if x == 0:
                if cell[1] < 3 or cell[1] > 7:
                    if cell[0] > 0:
                        result[0] = cell[0] - 1
                    else:
                        result[0] = cell[0]
                elif 4 <= cell[1] <= 7:
                    if cell[0] < 9:
                        result[0] = cell[0] + 1
                    else:
                        result[0] = cell[0]
                elif cell[1] == 3:
                    result[0] = cell[0]
            elif x == size - 1:
                if cell[size - 2] < 3 or cell[size - 2] > 7:
                    if cell[size - 1] > 0:
                        result[size - 1] = cell[size - 1] - 1
                    else:
                        result[size - 1] = cell[size - 1]
                elif 4 <= cell[size - 2] <= 7:
                    if cell[size - 1] < 9:
                        result[size - 1] = cell[size - 1] + 1
                    else:
                        result[size - 1] = cell[size - 1]
                elif cell[size - 2] == 3:
                    result[size - 1] = cell[size - 1]
            else:
                if (cell[x - 1] + cell[x + 1] < 3) or (cell[x - 1] + cell[x + 1] > 7):
                    if cell[x] > 0:
                        result[x] = cell[x] - 1
                    else:
                        result[x] = cell[x]
                elif 4 <= cell[x - 1] + cell[x + 1] <= 7:
                    if cell[x] < 9:
                        result[x] = cell[x] + 1
                    else:
                        result[x] = cell[x]
                elif cell[x - 1] + cell[x + 1] == 3:
                    result[x] = cell[x]

        for x in range(size):
            cell[x] = result[x]

    for index in range(size):
        print(cell[index], end=' ')
    print()
