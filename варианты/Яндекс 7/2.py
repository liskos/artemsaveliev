from itertools import *

def f(y, w, x, u):
    return (not ((not y or w) == x)) and u

for i in product([0, 1], repeat=3):
    t = [(0, 1, 0, i[0]), (0, 1, 1, 1), (1, 0, 1, i[1]), (1, i[2], 1, 1)]
    for p in permutations('ywxu'):
        if [f(**dict(zip(p, r))) for r in t] == [0, 0, 1, 1]:
            print(p, i)