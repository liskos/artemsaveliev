from itertools import *

def f(x, y, z, w):
    return (not x or y) and (not y or z) and (not z or w)

for i in product([0, 1], repeat=6):
    t = (i[0], i[1], 1, 0), (i[2], 0, i[3], 1), (1, i[4], 0, i[5])
    for p in permutations("xyzw"):
        s = "".join(p)
        if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
            print(s, i)
