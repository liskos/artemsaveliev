from itertools import *
k = 0
for x in product("КБЖЗФ", repeat=7):
    x = "".join(x)
    j = 0
    b = True
    for n in "КБЖЗФ":
        if x.count(n) > 3:
            b = False
    if b:
        for i in range(6):
            if x[i] == x[i + 1]:
                j += 1
        if j == 0:
            k += 1
print(k)