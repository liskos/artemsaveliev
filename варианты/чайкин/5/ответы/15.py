def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            ff = (x < y + a) or (x >= 37 - y) or (y <= a)
            if not ff:
                return False
    return True


for i in range(100):
    if f(i):
        print(i)
        break