def f(x, y, a):
    return ((a < x) or ((x**2 - 7*x + 10) > 0)) and ((a > y) or ((y*y + 7*y + 12) > 0))

for a in range(-1000, 1000):
    if all(f(x, y, a) == True for x in range(-1000, 1000) for y in range(-1000, 1000)):
        print(a)