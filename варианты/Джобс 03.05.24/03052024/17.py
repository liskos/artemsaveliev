a = [int(x) for x in open("17.txt")]
m = min([x for x in a if (len(str(abs(x))) == 2 and (x % (sum(map(int, str(x)))) == 0))])
b = []
for i in range(len(a) - 1):
    if (a[i] % m == 0) or (a[i + 1] % m == 0):
        b.append(a[i] + a[i + 1])
print(len(b), max(b))
