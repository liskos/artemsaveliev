def f(x, y):
    return (x + 1, y), (x * 2, y), (x, y + 1), (x, y * 2)

lst = [[" "] * 123*2 for _ in range(123*2)]

for x in range(123*2):
    for y in range(123*2):
        if x + y >= 123:
            lst[x][y] = "0"

for x in range(123):
    for y in range(123):
        if lst[x][y] == " " and any(lst[n][i] == "0" for n, i in f(x, y)):
            lst[x][y] = "1"

for x in range(123):
    for y in range(123):
        if lst[x][y] == " " and all(lst[n][i] == "1" for n, i in f(x, y)):
            lst[x][y] = "2"

for x in range(123):
    for y in range(123):
        if lst[x][y] == " " and any(lst[n][i] == "2" for n, i in f(x, y)):
            lst[x][y] = "3"

for x in range(123):
    for y in range(123):
        if lst[x][y] == " " and all(lst[n][i] in "13" for n, i in f(x, y)):
            lst[x][y] = "4"

for i in range(1, 200):
    print(*lst[i][1:], sep="\t")