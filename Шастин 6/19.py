def f(x, y):
    return (x-3, y), (x, y-3), ((x+1)//2, y), (x, (y+1)//2)

a = [[" "] * 600 for _ in range(600)]

for x in range(600):
    for y in range(600):
        if x + y <= 36:
            a[x][y] = "0"

for x in range(600):
    for y in range(600):
        if a[x][y] == " " and any(a[i][j] == "0" for i,j in f(x, y)):
            a[x][y] = "1"

for x in range(600):
    for y in range(600):
        if a[x][y] == " " and all(a[i][j] == "1" for i,j in f(x, y)):
            a[x][y] = "2"

for x in range(600):
    for y in range(600):
        if a[x][y] == " " and any(a[i][j] == "2" for i,j in f(x, y)):
            a[x][y] = "3"

for x in range(600):
    for y in range(600):
        if a[x][y] == " " and all(a[i][j] in "13" for i,j in f(x, y)):
            a[x][y] = "4"

for i in range(1, 600):
    print(*a[i][1:], sep="\t")