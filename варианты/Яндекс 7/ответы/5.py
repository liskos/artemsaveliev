def cm(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n = n // 7
    return s


def f(n):
    c = cm(n)
    if n % 7 == 0:
        c = c + c[-2:]
    else:
        c = c + cm(n % 7 * 2)
    return int(c, 7)


print(f(6), f(7))
for i in range(1, 1000):
    if f(i) < 220:
        print(i)
