def f(i, j):
    return (i - 3, j), (i, j - 3), ((i+1)//2, j), (i, (j+1)//2)


a = [[" "] * 600 for _ in range(600)]


for i in range(600):
    for j in range(600):
        if i + j <= 36:
            a[i][j] = "0"

for i in range(600):
    for j in range(600):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in f(i, j)):
            a[i][j] = "1"

for i in range(600):
    for j in range(600):
        if a[i][j] == " " and all(a[x][y] == "1" for x, y in f(i, j)):
            a[i][j] = "2"

for i in range(600):
    for j in range(600):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(600):
    for j in range(600):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i, j)):
            a[i][j] = "4"

for i in range(1,600):
    print(*a[i][1:], sep="\t")