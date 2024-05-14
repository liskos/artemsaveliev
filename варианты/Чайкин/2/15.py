def d(n, m):
    return n % m == 0

def f(x, a):
    return d(x, a) or not(d(x, 17) and d(x, 23))

for a in range(1, 1000):
    if all(f(x, a) for x in range(1000)):
        print(a)