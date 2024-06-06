from itertools import *

def f(x, y, w, z):
    return not((x == y) or (y == w) or (w == z)) or (x and not y)

for i in product([0, 1], repeat=6):
    t = {(i[0], 0, 0, 0), (0, 0, i[1], i[2]), (i[3], i[4], 1, i[5])}
    for p in permutations("xywz"):
        if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
            print(*p)