import functools


def prost():
    """находим список простых чисел до 50 000"""
    a = [2]
    for i in range(3, 1000000, 2):
        x = int(i ** 0.5)
        for j in a:
            if i % j == 0:
                break
            elif j >= x:
                continue
        else:
            a.append(i)
    return a


@functools.lru_cache(None)
def kol(n):
    k = set()
    for i in p:
        if n % i == 0:
            k.add(i)
    return k


def mult(a):
    p = set([])
    for x in a:
        p = p.union(kol(x))
        if len(p) > k:
            return p
    return p


import sys

sys.stdin = open("27B.txt")
n = int(input())
k = int(input())

p = prost()
a = [int(input()) for _ in range(n)]
s = 0
for i in range(1, n + 1):
    for t in range(n - i + 1):
        mm = mult(a[t:t + i])
        if len(mm) <= k:
            s += 1
print(s)
