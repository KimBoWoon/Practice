__author__ = 'user'

import turtle

a = turtle.Turtle()
a.penup()
a.goto(-50, -350)
a.pendown()


def fw_turn(length, angle):
    a.forward(length)
    a.left(angle)

a.color('red')
for i in range(0, 4):
    fw_turn(100, 90)
a.color('blue')
for i in range(0, 5):
    fw_turn(100, 72)
a.color('green')
for i in range(0, 6):
    fw_turn(100, 60)
a.color('yellow')
for i in range(0, 8):
    fw_turn(100, 45)
a.color('#ff00ff')
for i in range(0, 10):
    fw_turn(100, 36)
a.color('#eeeeee')
for i in range(0, 12):
    fw_turn(100, 30)
a.color('#00e2ad')
for i in range(0, 15):
    fw_turn(100, 24)
a.color('#000000')
for i in range(0, 20):
    fw_turn(100, 18)

a.color('#8e8e8e')
a.forward(50)
a.circle(50)

turtle.done()
