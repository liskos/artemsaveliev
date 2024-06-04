import itertools


def f(a, b, c, d):
    return (not a or b) and (not b or not c) and (c or d)


for a in itertools.product([0, 1], repeat=4):
    table = [(1, a[1], a[2], a[3]), (1, a[1], 1, a[3]), (1, a[1], 1, 1)]
    for p in itertools.permutations("abcd"):
        if len(set(table)) == 3 and [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
            print("".join(p))
