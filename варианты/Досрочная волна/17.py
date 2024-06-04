n = list(map(int, open("17_15333.txt")))
mx = []
for i in n:
    if i % 19 == 0:
        mx.append(i)
mx = max(mx)
lst = []
for i in range(len(n)-1):
    if n[i] > mx or n[i+1] > mx:
        lst.append(n[i]+n[i+1])
print(len(lst), max(lst))