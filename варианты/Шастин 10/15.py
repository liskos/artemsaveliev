def treug(n, m, k):
    return ((n + m) > k) and ((n + k) > m) and ((m + k) > n)

def f(x, a):
    return not treug(a, 7, x) or ((max(x + 5, 14) <= 27) == (not treug(36, 21, x)))

for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)