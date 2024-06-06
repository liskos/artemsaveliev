from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n < 3: return n + 3
    if n >= 3: return 4 * n + 6 + f(n - 2)

print(f(5117)-f(5113))