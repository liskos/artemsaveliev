from itertools import *

lst = []
for i in product("123456780", repeat=7):
    x = "".join(i)
    b = True
    if x[0] != "0":
        if x.count("6") == 1:
            for j in range(6):
                if int(x[j]) % 2 == int(x[j+1]) % 2:
                    b = False
                    continue
            if b:
                lst.append(1)
print(len(lst))