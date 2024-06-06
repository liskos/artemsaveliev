n = list(map(int, open("17.txt")))
sr = []
for i in n:
    if i % 2 == 1:
        sr.append(i)
sr = sum(sr)/len(sr)
lst = []
for i in range(len(n)-1):
    k = 0
    j = [n[i], n[i+1]]
    for z in j:
        if str(abs(z))[-2:] == "11":
            k += 1
    if k == 1 and sum(j) >= sr:
        lst.append(sum(j))
print(len(lst), max(lst))