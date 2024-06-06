from fnmatch import *

def dl(n):
    d = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    a = []
    for i in d:
        a.append(i)
    return a

def prov(n):
    return fnmatch(str(n), "*7?")

for i in range(400000, 500001):
    lst = dl(i)
    lst_ = list(map(prov, dl(i)))
    a = [j for j in lst if lst_[lst.index(j)]]
    if len(a) >= 18:
        print(i, sum(a), sep="\t")