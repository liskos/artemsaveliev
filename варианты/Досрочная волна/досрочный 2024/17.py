a = [int(i) for i in open("17.txt")]

m19 = max([i for i in a if i % 19 == 0])
rez = []
for i in range(len(a) - 1):
    if ((a[i] > m19) or (a[i + 1] > m19)):
        rez.append(a[i] + a[i + 1])
print(len(rez), max(rez))
