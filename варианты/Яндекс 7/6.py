from turtle import *
tracer(-1)
k = 30
lt(90)
rt(135)
for i in range(7):
    fd(7*k)
    rt(45)
    fd(8*k)
    rt(135)
up()
for x in range(-10, 20):
    for y in range(-30, 20):
        goto(x*k, y*k)
        dot(4)
exitonclick()
update()