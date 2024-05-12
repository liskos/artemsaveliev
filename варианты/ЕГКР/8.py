from itertools import *

lst = []
for x in product("0123456", repeat=7):
    x = "".join(x)
    k = 0
    if x[0] != "0":
        for i in x:
            if int(i) % 2 == 0:
                k += 1
        if k == 2:
            lst.append(x)

print(len(lst))