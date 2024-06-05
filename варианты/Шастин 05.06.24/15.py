def dl(n, m):
    return n % m == 0

def f(x, a):
    b = 120 <= x <= 180
    return dl(x, a) or (not b or (not dl(x, 16) or ((x + a) <= 204)))

for a in range(1, 1000):
    if all(f(x, a) for x in range(1000)):
        print(a)