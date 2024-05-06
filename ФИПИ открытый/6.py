from turtle import *
tracer(-1)
k = 10
for i in range(2):
    fd(21*k)
    rt(90)
    fd(27*k)
    rt(90)
up()
fd(9*k)
rt(90)
fd(10*k)
lt(90)
down()
for i in range(2):
    fd(86*k)
    rt(90)
    fd(47*k)
    rt(90)
up()
for x in range(-10, 30):
    for y in range(-40, 20):
        goto(x*k, y*k)
        dot(4)


exitonclick()
update()
