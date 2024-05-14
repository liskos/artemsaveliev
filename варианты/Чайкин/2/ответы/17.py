a = [int(x) for x in open("17.txt")]
m = max([x for x in a if str(x)[-3:] == "127"])

b = []
for i in range(len(a) - 2):
    z = a[i:i + 3]
    z1 = sorted(z)
    if z[1] == z1[1] and sum(z) % m == 0:
        b.append(sum(z))
print(len(b), max(b))
