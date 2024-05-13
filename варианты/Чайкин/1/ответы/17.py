def f(n):
    s1 = str(n % 6)
    s2 = str(n // 6 % 6)
    return s2 + s1


a = [int(i) for i in open("17.txt")]
m = max([x for x in a if f(x) == "23"])
rez = []
for i in range(len(a) - 2):
    z = a[i:i + 3]
    if [len(str(abs(n))) for n in z].count(4) == 1 and sum(z) % m == 0:
        rez.append(sum(z))
print(len(rez), max(rez))
