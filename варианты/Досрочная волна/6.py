from turtle import *
tracer(-1)
k = 20
for i in range(2):
    fd(13*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
fd(5*k)
rt(90)
fd(9*k)
lt(90)
down()
for i in range(2):
    fd(11*k)
    rt(90)
    fd(7*k)
    rt(90)

up()
for x in range(0, 20):
    for y in range(-40, 5):
        goto(x*k, y*k)
        dot(4)

exitonclick()
update()