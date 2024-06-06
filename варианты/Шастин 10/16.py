from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n > 1: return 2 * n + f(n - 1)

for i in range(1, 59000):
    f(i)

print(sum(map(int, str(f(57693))))**2)