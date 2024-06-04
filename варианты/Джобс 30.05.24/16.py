from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(10000)
@lru_cache()

def f(n):
    if n <= 1: return 1
    if n > 1: return f(n-1) - f(n-2) + 5

print(f(1040)-f(1015))