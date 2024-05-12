from itertools import *

def f(x, y, z, w):
    return (x or not y) and not (x == z) and w

def g(x, y, z, w):
    return (not x or y) and (not y or z) and (not z or w)

for i in product([0, 1], repeat=5):
    t = (1, 0, 0, i[0]), (1, i[1], 1, i[2]), (0, 0, i[3], i[4])
    for p in permutations("xyzw"):
        for j in product([0, 1], repeat=3):
            if [f(**dict(zip(p, r))) for r in t] == [j[0], j[1], 1] and [g(**dict(zip(p, r))) for r in t] == [1, 1, j[2]]:
                print(p, i)