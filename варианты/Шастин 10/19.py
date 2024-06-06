def f(x):
    return x + 1, x + 3, x * 4

lst = [" "] * 211*4
for x in range(211*4):
    if x >= 211:
        lst[x] = "0"

for x in range(211):
    if lst[x] == " " and any(lst[i] == "0" for i in f(x)):
        lst[x] = "1"

for x in range(211):
    if lst[x] == " " and all(lst[i] == "1" for i in f(x)):
        lst[x] = "2"

for x in range(211):
    if lst[x] == " " and any(lst[i] == "2" for i in f(x)):
        lst[x] = "3"

for x in range(211):
    if lst[x] == " " and all(lst[i] in "13" for i in f(x)):
        lst[x] = "4"

for x in range(211):
    if lst[x] == " " and any(lst[i] in "24" for i in f(x)):
        lst[x] = "5"

for i in range(1, 240):
    print(i, lst[i])
print("_________")
print("for 19")
for i in range(1, 240):
    if lst[i] == "2":
        print(i)
        break
print("for 20")
for i in range(1, 240):
    if lst[i] == "4":
        print(i)
print("for 21")
for i in range(1, 240):
    if lst[i] == "5":
        print(i)
        break