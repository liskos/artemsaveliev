import itertools


def f(x, y, z, w):
    return (x and not z) or (y == z) or not w


for a in itertools.product([0, 1], repeat=4):
    table = [(a[0], a[1], 0, 0), (1, 0, a[2], 0), (1, 0, 1, a[3])]
    for p in itertools.permutations("xyzw"):
        if len(set(table)) == 3 and [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
            print("".join(p))
