def f(n):
    oc = oct(n)[2:]
    if sum(int(x) for x in str(n)) % 2 == 0:
        oc = oc + str(n % 3)
    else:
        oc = max(x for x in oc) + oc
    return int(oc, 8)


print(f(6), f(5))
for i in range(1, 1000):
    if f(i) > 127:
        print(i)
        break
