a = [int(x) for x in open("17.txt")]
b = sorted(a)
m = b[-3]
c = []
for i in range(len(a) - 2):
    z = a[i:i + 3]
    if sum([1 for x in z if x % 2 == 0]) <= 2 and sum(z) <= m:
        c.append(sum(z))
print(len(c), max(c))
