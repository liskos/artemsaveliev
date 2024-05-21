from itertools import *
k = 0
for i in product("012345678", repeat=7):
    i = "".join(i)
    if i[0] != "0":
        if int(i[0]) % 2 == 0 and int(i[-1]) % 3 != 0 and i.count("6") >= 1:
            k += 1
print(k)