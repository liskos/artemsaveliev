from itertools import *

kombin = [i + z for i in "ВХ" for z in "ОУ"] + [z + i for i in "ВХ" for z in "ОУ"]
k = 0
for x in product("ВОЗДУХ", repeat=5):
    slovo = "".join(x)
    if slovo.count("У") + slovo.count("О") == 1:
        if not any(z in slovo for z in kombin):
            k += 1
print(k)