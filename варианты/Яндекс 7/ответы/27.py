import sys, functools
sys.stdin = open("27test.txt")
#TODO неработает


def s(z, k):
    """минимальная сумма прыжков по массиву с шагом к"""
    if len(z) == 0:
        return 0
    if len(z) <= k:
        return min(z)
    return min([s(z[i:], k) for i in range(1, k+1)])+z[0]


k, n = map(int, input().split())
z = [int(input()) for _ in range(n)]
print(s(z, k))
