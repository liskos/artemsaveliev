a = [int(x) for x in open("17.txt")]
min19 = min([x for x in a if x % 19 == 0])
b = []
for i in range(len(a)-1):
    if (a[i] % min19 == 0) or (a[i+1] % min19 == 0):
        b.append(a[i] + a[i + 1])
print(len(b), max(b))