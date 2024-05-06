from itertools import *

k = 0
for x in product("АПРСУ", repeat=5):
    x = "".join(x)
    k += 1
    if x.count("У") == 1:
        if x.find("У") == 4:
            if x[x.find("У")-1] != "А":
                print(k, x)
        if x.find("У") == 0:
            if x[x.find("У")+1] != "А":
                print(k, x)
        if x.find("У") > 0 and x.find("У") < 4:
            if x[x.find("У")-1] != "А" and x[x.find("У")+1] != "А":
                print(k, x)
    if x.count("У") == 0:
        print(k, x)