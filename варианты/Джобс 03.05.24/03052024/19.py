def f(i):
    return i - 10, i // 2


a = [" "] * 400
for i in range(400):
    if i < 20:
        a[i] = "0"

for i in range(400):
    if a[i] == " " and all(a[x] == "0" for x in f(i)):
        a[i] = "1"

for i in range(400):
    if a[i] == " " and any(a[x] == "1" for x in f(i)):
        a[i] = "2"

for i in range(400):
    if a[i] == " " and all(a[x] == "2" for x in f(i)):
        a[i] = "3"

for i in range(400):
    if a[i] == " " and any(a[x] in "13" for x in f(i)):
        a[i] = "4"

for i in range(400):
    if a[i] == " " and all(a[x] in "24" for x in f(i)):
        a[i] = "5"

for i in range(1, 400):
    print(i, a[i])
