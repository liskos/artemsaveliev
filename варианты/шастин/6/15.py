def f(a):
    b = range(34*10, 72*10+1)
    c = range(32*10, 61*10+1)
    for x in range(1, 1000):
        f = ((x not in b) or (x in a)) and ((x not in c) or (x in a))
        if not f:
            return False
    return True


m = 10000
s1 = 0
s2 = 10000
for a1 in range(0, 1000):
    for a2 in range(a1, 1000):
        if f(range(a1, a2+1)) and a2-a1 < m:
            s1 = a1
            s2 = a2
            m = a2 - a1
print(s1, s2)