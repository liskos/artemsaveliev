from itertools import *

def f(x, y, z, w):
    return ((not x or y) or (not z or w)) and not (not x or w)

for i in product([0, 1], repeat=5):
    t = (1, 0, 1, i[0]), (1, i[1], i[2], 1), (i[3], i[4], 1, 0)
    for p in permutations("xyzw"):
        s = "".join(p)
        if [f(**dict(zip(p, r))) for r in t] == [0, 1, 1]:
            print(s, i)