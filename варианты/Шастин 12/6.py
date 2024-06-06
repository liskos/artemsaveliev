from turtle import *
tracer(0)
k = 10
for i in range(2):
    fd(11*k)
    rt(90)
    fd(17*k)
    rt(90)
up()
fd(7*k)
lt(90)
bk(1*k)
rt(90)
down()
for i in range(2):
    fd(15*k)
    rt(90)
    fd(7*k)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(4)
done()
update()