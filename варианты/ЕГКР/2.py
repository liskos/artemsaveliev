from itertools import *

def f(x, y, w, z):
    return not (x or y) and not w or not (z or w) and y

for i in product([0, 1], repeat=8):
    t = (i[0], 1, i[1], i[2]), (i[3], i[4], 1, i[5]), (i[6], 1, i[7], 1)
    for p in permutations("xywz"):
        if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
            print(p, i)