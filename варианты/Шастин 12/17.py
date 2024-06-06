n = list(map(int, open("17.txt")))
mx = []
for i in n:
    if len(str(abs(i))) == 5 and str(i)[-1] == "7":
        mx.append(i)
mx = max(mx)
lst = []
for i in range(len(n)-2):
    l = [n[i], n[i+1], n[i+2]]
    k = 0
    for m in l:
        if str(m)[-2:] == "12":
            k += 1
    if k == 2 and sum(l) <= mx:
        lst.append(sum(l))
print(len(lst), abs(min(lst)))