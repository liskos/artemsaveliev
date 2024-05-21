def s(n):
    s = 0
    for poi in str(n):
        s += int(poi)
    return s

n = list(map(int, open("17_16264.txt")))
lst = []
for i in n:
    if len(str(i)) == 2 and i % s(i) == 0:
        lst.append(i)
mn = min(lst)
lst = []
for i in range(len(n)-1):
    if n[i] % mn == 0 or n[i + 1] % mn == 0:
        lst.append(n[i] + n[i + 1])
print(len(lst), max(lst))