__author__ = '보운'

import time, threading, sys


def count():
    for i in range(1, 11):
        time.sleep(1)
        if i > 10:
            print('땡')
            return
        if flag:
            print('정답')
            return
        print(10 - i)


th = threading.Thread(target=count)
th.start()
flag = False

while True:
    s = input()
    if s == 'A':
        flag = True
        sys.exit()
    else:
        print('오답')
