__author__ = '보운'

for t in range(int(input())):
    x = int(input())
    result = [0, 0, 0]
    for i in range(x):
        game = input().split()
        if game[0] == 'R':
            if game[1] == 'R':
                result[2] += 1
            elif game[1] == 'P':
                result[1] += 1
            elif game[1] == 'S':
                result[0] += 1
        if game[0] == 'P':
            if game[1] == 'R':
                result[0] += 1
            elif game[1] == 'P':
                result[2] += 1
            elif game[1] == 'S':
                result[1] += 1
        if game[0] == 'S':
            if game[1] == 'R':
                result[1] += 1
            elif game[1] == 'P':
                result[0] += 1
            elif game[1] == 'S':
                result[2] += 1

    for i in range(3):
        print(result[i], end=' ')
    print()