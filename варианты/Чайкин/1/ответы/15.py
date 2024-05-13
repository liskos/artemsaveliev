def f(a):
    for x in range(1, 10000):
        f = (x & a != 0) or ((x & 52 == 0) and (x & 14 == 0))
        if not f:
            return False
    return True


for a in range(1, 1000):
    if f(a):
        print(a)
        break
