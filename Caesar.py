__author__ = '보운'

for t in range(int(input())):
    move = int(input())
    data = input()
    cipherText = ''

    for i in range(len(data)):
        if 'A' <= data[i] <= 'Z':
            if chr(ord(data[i]) + move) > 'Z':
                cipherText += chr(ord(data[i]) + move - 26)
            else:
                cipherText += chr(ord(data[i]) + move)
        elif 'a' <= data[i] <= 'z':
            if chr(ord(data[i]) + move) > 'z':
                cipherText += chr(ord(data[i]) + move - 26)
            else:
                cipherText += chr(ord(data[i]) + move)
        else:
            cipherText += data[i]

    print(cipherText)