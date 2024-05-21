def tr(n):
    t = "012"
    s = ""
    while n > 0:
        s = t[n % 3] + s
        n = n // 3
    return s


def f(n):
    t = tr(n)
    if n % 2 == 2:
        t = "2" + t + tr(int(t[-1]) * 2)
    else:
        t = tr(int(t[0]) * 2) + t + "2"
    return int(t, 3)


a = []
for i in range(1, 1000):
    if f(i) > 100:
        a.append(f(i))
print(min(a))
