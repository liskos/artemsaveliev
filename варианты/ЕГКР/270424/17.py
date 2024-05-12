def f(x):
    return len(str(abs(x))) == 5 and str(abs(x))[-2:]=="21"

a = [int(x) for x in open("17.txt")]
m = max(x for x in a if len(str(abs(x))) == 5 and str(abs(x))[-2:] == "21")
rez = []
for i in range(len(a)-1):
    if f(a[i]) != f(a[i+1]) and ((a[i]**2 + a[i+1]**2) >= m**2):
        rez.append(a[i]+a[i+1])
print(len(rez), max(rez))
