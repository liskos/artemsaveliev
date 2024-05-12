def f(i):
    return i + 5, i * 3


a = [" "] * 1500

for i in range(1500):
    if i >= 435:
        a[i] = "0"

for i in range(435):
    if a[i] == " " and any(a[j] == "0" for j in f(i)):
        a[i] = "1"

for i in range(435):
    if a[i] == " " and all(a[j] == "1" for j in f(i)):
        a[i] = "2"

for i in range(435):
    if a[i] == " " and any(a[j] == "2" for j in f(i)):
        a[i] = "3"

for i in range(435):
    if a[i] == " " and all(a[j] in "13" for j in f(i)):
        a[i] = "4"

print("19)")
for i in range(1, 500):
    if a[i] == "2":
        print("s = ", i,"|||", a[i])
        break

print("20)")
for i in range(1, 500):
    if a[i] == "3":
        print("s = ", i,"|||", a[i])

print("21)")
for i in range(1, 500):
    if a[i] == "4":
        print("s = ", i,"|||", a[i])
        break
