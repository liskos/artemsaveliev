import itertools
a = []
for i in itertools.product(range(7), repeat=7):
    if i[0] != 0 and len([x for x in i if x % 2 == 0]) == 2:
        a.append(i)
print(len(a))
