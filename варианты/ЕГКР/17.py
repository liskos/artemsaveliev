n = list(map(int, open("17_16383.txt")))
lst = []
for i in n:
    if str(i)[-2:] == "21" and len(str(abs(i))) == 5: lst.append(i)
mx = max(lst)**2
a = []
for i in range(len(n)-1):
    j = [n[i], n[i+1]]
    k = 0
    for x in j:
        if str(x)[-2:] == "21" and len(str(abs(x))) == 5: k += 1
    if k == 1 and n[i]**2 + n[i+1]**2 >= mx:
        a.append(sum(j))
print(len(a), max(a))