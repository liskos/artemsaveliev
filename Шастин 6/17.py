n = open("17.txt")
n = list(map(int, n))
lst = []
for x in n:
    if x % 401 == 0:
        lst.append(x)
max = max(lst)
k = 0
ssum = []
for i in range(len(n)-2):
    n1 = sum(map(int, str(n[i])))
    n2 = sum(map(int, str(n[i+1])))
    n3 = sum(map(int, str(n[i+2])))
    if n1 != n2 and n2 != n3 and n1 != n3 and n[i] + n[i+1] + n[i+2] > max:
        k += 1
        ssum.append(n[i] + n[i+1] + n[i+2])
print(k, min(ssum))