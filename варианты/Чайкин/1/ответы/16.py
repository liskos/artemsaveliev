import sys

sys.setrecursionlimit(3000)


def f(x):
    if x < 3:
        return 1
    return 2 * x - 1 + f(x - 2)


print(f(3033))
