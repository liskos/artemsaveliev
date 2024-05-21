def f(a):
    for x in range(-500, 500):
        for y in range(-500, 500):
            ff = ((a < x) or (x * x - 7 * x + 10 > 0)) and ((a >= y) or (y * y + 7 * y + 12 > 0))
            if not ff:
                return False
    return True


for a in range(-300, 300):
    if f(a):
        print(a)
