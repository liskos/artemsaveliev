from itertools import *

lst = []
for x in product("0123456789abcdefg", repeat=6):
    x = "".join(x)
    if x[0] != "0":
        b = True
        for i in "2357bd":
            if x.count(i) != 0:
                b = False
        k = 0
        if b:
            if int(x[0], 17) % 2 == 0:
                for z in x:
                    if x.count(z) == 1:
                        k += 1
                if k == 6:
                    lst.append(x)
print(len(lst))