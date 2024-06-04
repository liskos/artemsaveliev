n = list(map(int, open("17_17097.txt")))
a = []
lst = []
for i in n:
    if str(i)[-2:] == "17":
        a.append(i)
mn = min(a)
for i in range(len(n)-2):
    if n[i+1] % mn == 0:
        lst.append(n[i] + n[i+2])
print(len(lst), max(lst))