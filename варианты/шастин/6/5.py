def ch(n):
    t = "0123"
    s = ""
    while n > 0:
        s = t[n % 4] + s
        n = n // 4
    return s


def f(n):
    c = ch(n)
    if n % 3 == 0:
        c = c[-1] + c[1:-1] + c[0] + "1"
    else:
        c = c + str(n % 3)
    return int(c, 4)


print(f(11), f(13))
a = []
for i in range(1, 1000):
    if f(i) <= 340:
        a.append(f(i))
print(max(a))