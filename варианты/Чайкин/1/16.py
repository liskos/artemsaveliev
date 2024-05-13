from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n < 3: return 1
    if n > 2: return 2 * n - 1 + f(n - 2)

print(f(3033))