from turtle import *
tracer(0)
k = 10
for i in range(2):
    fd(8*k)
    rt(90)
    fd(12*k)
    rt(90)
up()
bk(3*k)
lt(90)
fd(5*k)
rt(90)
down()
for i in range(4):
    fd(5*k)
    rt(90)
    fd(14*k)
    rt(90)
up()
fd(10*k)
down()
for i in range(4):
    fd(8*k)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(4)

exitonclick()
update()