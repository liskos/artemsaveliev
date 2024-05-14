from itertools import *

k = 0
lst = []
for x in product("ЕИКРСУЯ", repeat=6):
    x = "".join(x)
    k += 1
    a = []
    for j in "ЕИУЯ":
        a.append(x.count(j))
    if k % 2 == 0 and sum(a) <= 2 and x[0] != "К":
        lst.append(x)
print(len(lst))