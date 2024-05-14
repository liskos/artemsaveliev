n = list(map(int, open("17_9946.txt")))
a = []
for i in n:
    if str(i)[-3:] == "127":
        a.append(i)
mx = max(a)
lst = []
for i in range(len(n)-2):
    j = [n[i], n[i+1], n[i+2]]
    j.sort()
    if ((j[0] < n[i+1] < j[2]) or (j[0] > n[i+1] > j[2])) and sum(j) % mx == 0:
        lst.append(n[i] + n[i+1] + n[i+2])
print(len(lst), max(lst))