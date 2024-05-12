def f(n):
    n = bin(n)[2:]
    l = n[1::2]
    if l.count("0") > l.count("1"):
        n = n.replace("0", "2")
        n = n.replace("1", "0")
        n = n.replace("2", "1")
    else:
        for i in range(1, len(n), 2):
            n = n[:i] + "1" + n[i + 1:]
    return int(n, 2)


lst = []
a = []
for i in range(28, 5000):
    if f(i) <= 1337:
        lst.append(f(i))
        a.append(i)
print(a[lst.index(max(lst))], max(lst))