n = list(map(int, open("17_10126.txt")))

def sh(n):
    s = ""
    while n > 0:
        s += str(n % 6)
        n //= 6
    return s[::-1]

a = []
for i in n:
    if sh(i)[-2:] == "23":
        a.append(i)
mx = max(a)
lst = []
for i in range(len(n)-2):
    j = [n[i], n[i+1], n[i+2]]
    k = 0
    for z in j:
        if len(str(abs(z))) == 4:
            k += 1
    if k == 1 and sum(j) % mx == 0:
        lst.append(sum(j))
print(len(lst), max(lst))