from itertools import *

lst = []
y = [i + z + i for i in "ВХ" for z in "ОУ"] + [i + z for i in "ВХ" for z in "ОУ"] + [z + i for i in "ВХ" for z in "ОУ"]
lst = []
for x in product("ВОЗДУХ", repeat=5):
    x = "".join(x)
    if x.count("У") == 1 or x.count("О") == 1:
        k = 0
        for z in y:
            if z in x:
                k += 1
                continue
        if k == 0: lst.append(x)

print(len(lst))