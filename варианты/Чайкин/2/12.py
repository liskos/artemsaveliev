def de(n):
    a = set()
    for i in range(1, n+1):
        if n % i == 0:
            a.add(i)
    return a

def su(n):
    a = []
    for i in n:
        a.append(int(i))
    return sum(a)

lst = []
for i in range(4, 1000):
    n = "3" + "5"*i
    while "25" in n or "355" in n or "555" in n:
        if "25" in n:
            n = n.replace("25", "32", 1)
        if "355" in n:
            n = n.replace("355", "25", 1)
        if "555" in n:
            n = n.replace("555", "3", 1)
    if len(de(su(n))) == 2:
        lst.append(n)
print(len(lst))