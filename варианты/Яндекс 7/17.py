n = open("17.txt")
n = list(map(int, n))
tr = n
tr.sort()
a = []
for i in range(len(n)-2):
    lst = []
    k = 0
    lst = [n[i], n[i+1], n[i+2]]
    for x in lst:
        if x % 2 == 0:
            k += 1
    lst.sort()
    if k <= 2 and sum(lst) <= tr[-3]:
        a.append(sum(lst))
print(len(a), max(a))