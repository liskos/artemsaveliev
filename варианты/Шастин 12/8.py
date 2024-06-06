from itertools import *

k = 0
for x in product("АБИЛМСУЦЯ", repeat=5):
    x = "".join(x)
    k += 1
    j = 0
    if x[-1] != "Я" and k % 2 == 1:
        for i in x:
            if i in "АИУЯ":
                j += 1
        if j == 2:
            print(x, k)