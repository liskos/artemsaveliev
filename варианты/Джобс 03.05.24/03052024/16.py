import sys, functools

sys.setrecursionlimit(10000)


@functools.lru_cache(None)
def f(n):
    if n == 2500:
        return -2495
    if n < 7:
        return 7
    if (n >= 7) and (n % 3 != 0):
        return 5 - f(n - 1)
    return 3 + f(n - 1)


print(f(3015))
