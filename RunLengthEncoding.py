__author__ = '보운'

for t in range(int(input())):
    flag, data = input().split()
    flag = int(flag)
    data += '0'
    result = ''
    size = len(data)
    cnt = 1
    zipSize = 0

    if flag == 0:
        c = data[0]

        for i in range(1, size):
            if cnt > 255:
                result += '0' + c
                cnt = 1
                zipSize += 2
                c = data[i]
            elif c == data[i]:
                cnt += 1
            elif c != data[i]:
                result += str(cnt) + c
                cnt = 1
                zipSize += 2
                c = data[i]

        print(size - 1, zipSize, result)

    elif flag == 1:
        chrSize = ''

        for i in range(size - 1):
            if data[i] == '0':
                chrSize = '256'
            elif '1' <= data[i] <= '9':
                chrSize += data[i]
            else:
                result += data[i] * int(chrSize)
                chrSize = ''
                zipSize += 2

        print(len(result), zipSize, result)