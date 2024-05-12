def f(x, y, a):
    return (x < y + a) or (x >= 37 - y) or (y <= a)

for a in range(1000):
    if all(f(x, y, a) == 1 for x in range(1000) for y in range(1000)):
        print(a)
        break