__author__ = '보운'

import os

file = os.open("input.txt", os.O_CREAT | os.O_RDWR)

os.dup2(file, 0)

print(input())

os.close(file)