def s(n):
    return sum(map(int, str(n)))


a = [int(x) for x in open("17.txt")]
m = max([x for x in a if x % 401 == 0])
z = []
for i in range(len(a)-2):
    n = [s(a[i]), s(a[i + 1]), s(a[i + 2])]
    if len(set(n)) == 3 and  (a[i] + a[i+1] + a[i + 2] > m):
        z.append(a[i] + a[i+1] + a[i + 2])
print(len(z), min(z), sep="\t")