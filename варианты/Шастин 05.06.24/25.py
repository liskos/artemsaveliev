from fnmatch import *

def f(n):
    l = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            l.add(i)
            l.add(n // i)
    lst = []
    for i in l:
        lst.append(i)
    lst.sort()
    return lst

a = []
for x in range(1, 10**9//2068 + 1):
    x = str(x * 2068)
    if fnmatch(x, "193*7?") and sum(f(int(x))[1:-2]) % 7 == 0:
        print(x, sum(f(int(x))[1:-2]), sep="\t")