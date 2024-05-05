from turtle import *
tracer(-1)
k = 10
for i in range(4):
    fd(16*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
rt(90)
fd(10*k)
lt(90)
fd(10*k)
down()
for i in range(4):
    fd(15*k)
    rt(90)
up()
fd(1*k)
lt(90)
fd(1*k)
rt(90)
down()
for i in range(7):
    fd(12*k)
    rt(90)

up()
for x in range(-10, 20):
    for y in range(-30, 20):
        goto(x*k, y*k)
        dot(4)
exitonclick()
update()