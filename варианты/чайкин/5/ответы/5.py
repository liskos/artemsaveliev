def f(n):
    b = bin(n)[2:]
    if b[1::2].count("0") > b[1::2].count("1"):
        b1 = b.replace("1","2")
        b1 = b1.replace("0","1")
        b1 = b1.replace("2", "0")
    else:
        b1 = ""
        for i in range(len(b)):
            if i % 2 == 1:
                b1 += "1"
            else:
                b1 += b[i]
    return int(b1, 2)


a = []
for i in range(1, 100000):
    if f(i) <= 1337:
        a.append(f(i))
m = max(a)
for i in range(1, 100000):
    if f(i) == m:
        print(i)
        break

