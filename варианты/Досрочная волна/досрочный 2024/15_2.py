def f(a):
    global b, c
    for x in range(1, 1000 * k):
        ff = (x not in c) or (not ((x not in a) and (x in b)) or (x not in c))
        if not ff:
            return False
    return True


k = 10
b = range(24 * k, 90 * k + 1)
c = range(47 * k, 115 * k + 1)
m = 1000 * k
s1, s2 = 0, 0
for a1 in range(20 * k, 120 * k):
    for a2 in range(a1, 120 * k):
        a = range(a1, a2 + 1)
        if f(a) and (a2 - a1 < m):
            m = a2 - a1
            s2 = a2
            s1 = a1
print(m / k, s1 / k, s2 / k)
