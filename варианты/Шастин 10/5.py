def dv(n):
    lst = []
    while n > 0:
        lst.append(n % 12)
        n //= 12
    a = ""
    for i in lst:
        if i == 10: a += "a"
        if i == 11: a += "b"
        else: a += str(i)
    return a[::-1]


def f(n):
    ch = dv(n)
    if n % 3 == 0: ch = "1" + ch + "b"
    else: ch = "2" + ch + "0"
    return int(ch, 12)

print(f(11), f(12))
a = []
for i in range(1000):
    if f(i) < 1996:
        a.append(f(i))
print(max(a))