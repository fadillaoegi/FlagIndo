# @fdlml_
from operator import lt
from turtle import bgcolor, color, down, exitonclick, fd, forward, goto, rt, shape, speed
from turtle import *

bgcolor("black")
shape('turtle')

forward(50)

up()
goto(0, 0)
down()

for i in range(2):
    fd(200)
    rt(90)
    fd(80)
    rt(90)

colo('red')
speed(70)

for i in range(30):
    fd(150)
    rt(90)
    fd(1)
    rt(90)
    fd(150)
    lt(90)
    fd(1)
    lt(90)

color('white')

for i in range(30):
    fd(150)
    rt(90)
    fd(1)
    rt(90)
    fd(150)
    lt(90)
    fd(1)
    lt(90)


fd(150)
exitonclick()
