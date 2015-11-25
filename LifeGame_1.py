__author__ = '보운'

for t in range(int(input())):
    size, time = input().split()
    size = int(size)
    time = int(time)

    temp = input().split()
    cell = [0] * (size + 2)
    result = [0] * (size + 2)
    for i in range(1, size + 1):
        cell[i] = int(temp[i - 1])

    for i in range(time):
        for x in range(1, size + 1):
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

        for x in range(1, size + 1):
            cell[x] = result[x]

    for index in range(1, size + 1):
        print(cell[index], end=' ')
    print()