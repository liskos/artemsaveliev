def dl(n ,m):
    return n % m == 0

def f(x, a):
    return not (not dl(x, a)) or (not dl(x, 28) or (not dl(x, 49)))

for a in range(1, 1000):
    if all(f(x, a) for x in range(1000)):
        print(a)