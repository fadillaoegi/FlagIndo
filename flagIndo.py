
from turtle import *

bgcolor("black")
forward(50)

shape('turtle')
tracer(1)

up()
goto(0, 0)
down()

for i in range(2):
    fd(200)
    rt(90)
    fd(80)
    rt(90)

color('red')
speed(50)
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
