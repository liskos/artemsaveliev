from turtle import *
tracer(-1)
k = 10
for i in range(2):
    fd(23*k)
    lt(90)
    bk(27*k)
    lt(90)
up()
bk(5*k)
rt(90)
fd(11*k)
lt(90)
down()
for i in range(2):
    fd(26*k)
    rt(90)
    fd(32*k)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(4)
exitonclick()
update()