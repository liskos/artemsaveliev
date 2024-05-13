def tr(n):
    t = "012"
    s = ""
    while n > 0:
        s = t[n % 3] + s
        n = n // 3
    return s


def f(n):
    t = tr(n)
    if n % 4 == 0:
        t = t + t[-3:]
    else:
        t = t + tr(n % 4 * 4)
    return int(t, 3)


a = []
for i in range(1, 1000):
    if f(i) < 127:
        a.append(f(i))
print(max(a))
