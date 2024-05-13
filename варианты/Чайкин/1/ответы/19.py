def f(i):
    return i + 1, i + 2, i * 3


a = [" "] * 800

for i in range(800):
    if i >= 248:
        a[i] = "0"

for i in range(248):
    if a[i] == " " and any(a[j] == "0" for j in f(i)):
        a[i] = "1"

for i in range(248):
    if a[i] == " " and all(a[j] == "1" for j in f(i)):
        a[i] = "2"

for i in range(248):
    if a[i] == " " and any(a[j] == "2" for j in f(i)):
        a[i] = "3"

for i in range(248):
    if a[i] == " " and all(a[j] in "13" for j in f(i)):
        a[i] = "4"

for i in range(1, 250):
    print(i, a[i])
