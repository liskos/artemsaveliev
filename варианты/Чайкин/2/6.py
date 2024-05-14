from turtle import *
tracer(-1)
k = 20
for i in range(3):
    fd(9*k)
    rt(90)
    fd(7*k)
    rt(90)
up()
fd(3*k)
rt(90)
bk(-5*k)
lt(90)
down()
for i in range(2):
    fd(10*k)
    lt(90)
    fd(5*k)
    lt(90)

up()
for x in range(-20, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(4)
exitonclick()
update()