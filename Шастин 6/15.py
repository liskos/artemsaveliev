from itertools import *

def f(x):
    b = 34 <= x <= 72
    c = 32 <= x <= 61
    a = a1 <= x <= a2
    return (not b or a) and (not c or a)

ox = [i/4 for i in range(32*4, 73*4)]
lst = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) == 1 for x in ox):
        lst.append(a2 - a1)
print(min(lst))