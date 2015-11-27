__author__ = '보운'

for t in range(int(input())):
    button = [
        ['.-\''], ['ABC'], ['DEF'],
        ['GHI'], ['JKL'], ['MNO'],
        ['PQRS'], ['TUV'], ['WXYZ'],
        [''], ['+'], [' '],
    ]
    cnt = 0
    data = input()
    data += '1'
    c = data[0]
    result = ''
    i = 1

    while i < len(data):
        if c == '*':
            c = data[i]
        elif c == data[i]:
            cnt += 1
        elif data[i] != c:
            if data[i] == '*':
                result += button[int(c) - 1][0][cnt % len(button[int(c) - 1][0])]
                cnt = 0
                i += 1
                c = data[i]
            elif data[i] == '0':
                result += '+'
            elif data[i] == '#':
                result += ' '
            else:
                result += button[int(c) - 1][0][cnt % len(button[int(c) - 1][0])]
                cnt = 0
                c = data[i]

        i += 1

    print(result)