n = open("17_16328.txt")
n = list(map(int, n))
lst = []
for x in n:
    if x % 19 == 0: lst.append(x)
min = min(lst)
a = []
for i in range(len(n)-1):
    if n[i] % min == 0 or n[i + 1] % min == 0: a.append(n[i] + n[i+1])
print(len(a), max(a))