from itertools import *

def f(w, z, y, x):
    return not(not w or (z == y)) and (not x or y)

for i in product([0, 1], repeat=5):
    t = [i[0], 1, 1, i[1]], [0, i[2], i[3], 0], [i[4], 0, 1, 0]
    for p in permutations("wzyx"):
        if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
            print("".join(p), i)