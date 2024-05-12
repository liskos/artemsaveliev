def de(n, m):
    return n % m == 0

def f(x, a):
    return not (not de(x, a)) or (not de(x, 28) or (not de(x, 49)))

for a in range(1, 1000):
    if all(f(x, a) == 1 for x in range(1, 1000)):
        print(a)