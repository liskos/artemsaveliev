from itertools import *

def f(z, w, x, y):
    return (z and not w) or (z == x) or y

for i in product([0, 1], repeat=4):
    t = [i[0], i[1], 0, 1], [1, 0, i[2], 1], [1, 1, 0, i[3]]
    for p in permutations("zwxy"):
        if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
            print("".join(p), i)