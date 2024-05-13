def f(x, a):
    return (x & a != 0) or ((x & 52 == 0) and (x & 14 == 0))

for a in range(500):
    if all(f(x, a) == 1 for x in range(500)):
        print(a)
        break