def f(x, y):
    return (x-2, y), (int(x/2+0.5), y), (x, y-2), (x, int(y/2+0.5))

lst = [[" "] * 108*2 for _ in range(108*2)]
for x in range(108*2):
    for y in range(108*2):
        if x + y <= 108:
            lst[x][y] = "0"

for x in range(108*2):
    for y in range(108*2):
        if lst[x][y] == " " and any(lst[n][i] == "0" for n, i in f(x, y)):
            lst[x][y] = "1"

for x in range(108*2):
    for y in range(108*2):
        if lst[x][y] == " " and all(lst[n][i] == "1" for n, i in f(x, y)):
            lst[x][y] = "2"

for x in range(108*2):
    for y in range(108*2):
        if lst[x][y] == " " and any(lst[n][i] == "2" for n, i in f(x, y)):
            lst[x][y] = "3"

for x in range(108*2):
    for y in range(108*2):
        if lst[x][y] == " " and all(lst[n][i] in "13" for n, i in f(x, y)):
            lst[x][y] = "4"

for i in range(1, 108*2):
    print(*lst[i][1:], sep="\t")