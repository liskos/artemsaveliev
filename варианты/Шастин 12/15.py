from itertools import *

def f(x):
    b = 54 <= x <= 120
    c = 78 <= x <= 151
    a = a1 <= x <= a2
    return not c or (not (b and not a) or (not c))

lst = []
ox = [i/4 for i in range(54*4, 151*4)]
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        lst.append(a2 - a1)
print(min(lst))