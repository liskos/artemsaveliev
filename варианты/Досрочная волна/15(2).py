from itertools import *

def f(x):
    b = 24 <= x <= 90
    c = 47 <= x <= 115
    a = a1 <= x <= a2
    return not c or (not (not a and b) or (not c))

ox = [i/4 for i in range(24*4, 115*4)]
lst = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        lst.append(a2-a1)
print(min(lst))