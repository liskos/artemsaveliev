from itertools import *

def f(a, b, c, d):
    return (not a or b) and (not b or (not c)) and (not (not c) or d)

for i in product([0, 1], repeat=6):
    t = (1, i[0], i[1], i[2]), (1, i[3], 1, i[4]), (1, i[5], 1, 1)
    for p in permutations("abcd"):
        s = "".join(p)
        if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
            print(s, i)