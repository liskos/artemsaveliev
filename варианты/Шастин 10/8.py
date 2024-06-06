from itertools import *

usl = [str(i)+"7" for i in range(2, 9, 2)] + ["a7", "7a"] + ["7" + str(i) for i in range(2, 9, 2)]
lst = []
for i in product("123456789ab0", repeat=5):
    x = "".join(i)
    if x.count("a") == 2 and x[0] != "0":
        b = True
        for j in range(4):
            if x[j] + x[j+1] in usl:
                b = False
        if b:
            lst.append(x)
print(len(lst))