def f(x, a):
    return ((x | 26) < 42) or ((x | 36) > 68) or ((x | 12) > a)

for a in range(10000):
    if all(f(x, a) for x in range(10000)):
        print(a)
