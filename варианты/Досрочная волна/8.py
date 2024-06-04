from itertools import *

k = 0
l = ["АА", "ААА", "АААА", "ААААА"]
for x in product("АПРСУ", repeat=5):
    x = "".join(x)
    k += 1
    b = True
    if x.count("У") <= 1:
        for i in l:
            if i in x:
                b = False
        if b:
            print(k, x)
            break