n = list(map(int, open("17_10004.txt")))
a = []
for i in range(len(n)-2):
    lst = [n[i], n[i+1], n[i+2]]
    k = 0
    for x in lst:
        if len(str(x)) != 4:
            k += 1
    if sum(lst) > 0:
        if k == 1 and str((sum(lst)**0.5) % 2) in "1.0 0.0":
            a.append(sum(lst))
print(len(a), min(a))