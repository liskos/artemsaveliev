from itertools import *

def f(x, z, y, w):
    return (x and not z) or (y == z) or not w

for i in product([0, 1], repeat=4):
    t = [i[0], i[1], 0, 0], [1, 0, i[2], 0], [1, 0, 1, i[3]]
    for p in permutations("xzyw"):
        if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
            print("".join(p), i)