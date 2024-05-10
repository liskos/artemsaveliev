def f(a):
    for x in range(0, 300):
        for y in range(0, 300):
            ff = ((x >= a) or (121 >= x * x)) and ((y * y < 49) or (a < y))
            if not ff:
                return False
    return True


for a in range(0, 300):
    if f(a):
        print(a)
