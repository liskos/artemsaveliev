def f(x):
    return x + 1, x + 4, x * 3

lst = [" "] * 200

for i in range(200):
    if i >= 53:
        lst[i] = "0"

for i in range(53):
    if lst[i] == " " and any(lst[x] == "0" for x in f(i)):
        lst[i] = "1"

for i in range(53):
    if lst[i] == " " and all(lst[x] == "1" for x in f(i)):
        lst[i] = "2"

for i in range(53):
    if lst[i] == " " and any(lst[x] == "2" for x in f(i)):
        lst[i] = "3"

for i in range(53):
    if lst[i] == " " and all(lst[x] in "13" for x in f(i)):
        lst[i] = "4"

print("for 19")
for i in range(1, 100):
    if i % 3 == 0 and lst[i] == "1":
        print(i // 3)
        break

print("for 20")
for i in range(1, 100):
    if lst[i] == "3":
        print(i)

print("for 21")
for i in range(1, 100):
    if lst[i] == "4":
        print(i)
        break