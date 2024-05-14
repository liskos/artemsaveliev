def f(x, y):
    return (x+2, y), (x+6, y), (x*3, y), (x, y+2), (x, y+6), (x, y*3)

lst = [[" "] * 288*3 for _ in range(288*3)]

for x in range(288*3):
    for y in range(288*3):
        if x + y >= 288:
            lst[x][y] = "0"

for x in range(288):
    for y in range(288):
        if lst[x][y] == " " and any(lst[n][i] == "0" for n, i in f(x, y)):
            lst[x][y] = "1"

for x in range(288):
    for y in range(288):
        if lst[x][y] == " " and all(lst[n][i] == "1" for n, i in f(x, y)):
            lst[x][y] = "2"

for x in range(288):
    for y in range(288):
        if lst[x][y] == " " and any(lst[n][i] == "2" for n, i in f(x, y)):
            lst[x][y] = "3"

for x in range(288):
    for y in range(288):
        if lst[x][y] == " " and all(lst[n][i] in "13" for n, i in f(x, y)):
            lst[x][y] = "4"

for i in range(1, 100):
    print(*lst[i][1:], sep="\t")