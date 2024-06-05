n = list(map(int, open("17.txt")))
mx = []
for i in n:
    if len(str(abs(i))) == 4 and str(i)[-2:] == "22":
        mx.append(i)
mx = max(mx)
lst = []
for i in range(len(n)-2):
    z = [n[i], n[i + 1], n[i + 2]]
    if sum(z) >= mx and len(str(abs(z[0]))) != len(str(abs(z[1]))) and len(str(abs(z[1]))) != len(str(abs(z[2]))) and len(str(abs(z[2]))) != len(str(abs(z[0]))):
        lst.append(sum(z))
print(len(lst), max(lst))