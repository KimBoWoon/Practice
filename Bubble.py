__author__ = '보운'

sortList = input().split()
sortList = [99, 81, 700, 6, 5005, 444, 321, 23456, 1]
size = len(sortList)
for i in range(size):
    sortList[i] = int(sortList[i])

for x in range(size - 1):
    for y in range(size - 1):
        if sortList[y] > sortList[y + 1]:
            temp = sortList[y]
            sortList[y] = sortList[y + 1]
            sortList[y + 1] = temp

    for i in range(size):
        print(str(sortList[i]), end=' ')
    print()