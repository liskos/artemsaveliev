def d(n, m):
    return n % m == 0

def f(x, a):
    return not (not d(x, a)) or (not d(x, 14) or not d(x, 4))

for a in range(1, 600):
    if all(f(x, a) == 1 for x in range(500)):
        print(a)