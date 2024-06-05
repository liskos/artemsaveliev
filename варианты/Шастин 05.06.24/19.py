def f(x):
    return x + 1, x + 2, x * 2

lst = [" "] * 112*2
for x in range(112*2):
    if x >= 112:
        lst[x] = "0"

for x in range(112):
    if lst[x] == " " and any(lst[i] == "0" for i in f(x) if i % 2 == 0):
        lst[x] = "1"

for x in range(112):
    if lst[x] == " " and all(lst[i] == "1" for i in f(x) if i % 2 == 0):
        lst[x] = "2"

for x in range(112):
    if lst[x] == " " and any(lst[i] == "2" for i in f(x) if i % 2 == 0):
        lst[x] = "3"

for x in range(112):
    if lst[x] == " " and all(lst[i] in "13" for i in f(x) if i % 2 == 0):
        lst[x] = "4"

for i in range(1, 150):
    print(i, lst[i])
print("_________")
print("for 19")
for i in range(1, 150):
    if i % 2 == 0 and lst[i] == "1":
        print(i//2)
        break
print("for 20")
for i in range(1, 150):
    if lst[i] == "3":
        print(i)
print("for 21")
for i in range(1, 150):
    if lst[i] == "4":
        print(i)
        break