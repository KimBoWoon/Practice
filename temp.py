__author__ = 'user'

import datetime, time

dt_now = datetime.datetime.now()
dt_delta = datetime.timedelta(seconds=1)

while True:
    dt_now = dt_now - dt_delta
    print(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)

import datetime
import time
import random

now = datetime.datetime.now()
delta = datetime.timedelta(minutes=1)

while True:
    now = now + delta
    file_name = now.strftime("%Y-%m-%d_DATA")
    data_time = now.strftime("%Y-%m-%d %H:%M")
    d1 = random.randrange(0, 9999)
    d2 = random.randrange(0, 9999)
    d3 = random.randrange(0, 9999)
    data = '{0}, {1:4d}, {2:4d}, {3:4d}\n'.format(data_time, d1, d2, d3)

    with open(file_name, 'a') as f:
        f.write(data)
    time.sleep(1 / 1000)

import glob

l = glob.glob('/home/user/PycharmProjects/practice/*_DATA')
l.sort()

for x in range(0, len(l)):
    s = ''
    with open(l[x], 'r') as f:
        s = f.read()

    with open('DATA', 'a') as f:
        f.write(s)