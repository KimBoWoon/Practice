__author__ = 'user'

import turtle
import random

t = turtle.Turtle()
screen = t.getscreen()
w = 150
screen.setworldcoordinates(-w, -w, w, w)

size = 260
step = 20

t.up()
t.goto(-w, -(w / 2))
t.down()
t.left(90)
t.forward(200)
t.up()
t.right(90)
t.goto(-w, -(w / 2))
t.down()
t.forward(200)
t.up()
t.goto(-w, -(w / 2))

colorList = ['red', 'green', 'blue']
for i in range(3):
    t.color(colorList[i])
    l = []
    for j in range(size):
        l.append(random.randrange(-30, 30))
    t.down()
    for x in range(0, size, step):
        t.goto(-w + x, -(w / 2) + int(l[x]) + random.randrange(0, 50))
    t.up()
    t.goto(-w, -(w / 2))

turtle.done()