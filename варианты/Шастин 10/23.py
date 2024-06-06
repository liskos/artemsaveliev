n = {5}
for i in range(7):
    k = set()
    for j in n:
        k.add(j + 7)
        k.add(j + 5)
        k.add(j - 3)
    n = k.copy()
print(len(n))