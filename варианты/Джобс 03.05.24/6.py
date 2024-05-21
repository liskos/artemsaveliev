from turtle import *
tracer(-1)
screensize(10000, 10000)
k = 10
rt(45)
for i in range(10):
    rt(45)
    fd(203*k)
    rt(45)
up()
bk(40*k)
rt(45)
down()
for i in range(5):
    fd(20*k)
    lt(90)
up()
for x in range(-194, -174):
    for y in range(-231, -211):
        goto(x*k, y*k)
        dot(4)
exitonclick()
update()