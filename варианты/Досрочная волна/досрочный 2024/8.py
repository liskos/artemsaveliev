import itertools

a = ["".join(i) for i in itertools.product("АПРСУ", repeat=5)]
k = 0
for i in a:
    k += 1
    if (i.count("У") <= 1) and ("АА" not in i):
        print(k, i)
        break
