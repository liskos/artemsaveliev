import itertools


def f(x, y, u, w):
    return (not ((not y or w) == x)) and u


z = itertools.product([0, 1], repeat=4)  # всевозможные комбинации 0000 0001 0010 ...
for i in z:
    t = [(0, 1, 0, i[3]), (0, 1, 1, 1), (1, 0, 1, i[3]), (1, i[1], 1, 1)]
    for p in itertools.permutations("xyuw"):  # перебираем всевозможные перемещения (16 шт)
        if [f(**dict(zip(p, r))) for r in t] == [0,0,1,1]:
            print(p , i)


