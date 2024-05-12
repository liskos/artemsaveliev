def f(i, j):
    return (i + 2, j), (i, j + 2), (i * 3, j), (i, j * 3)


a = [[" "] * 500 for _ in range(500)]

for i in range(500):
    for j in range(500):
        if i + j >= 150:
            a[i][j] = "0"

for i in range(150):
    for j in range(150):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in f(i, j)):
            a[i][j] = "1"

for i in range(150):
    for j in range(150):
        if a[i][j] == " " and all(a[x][y] == "1" for x, y in f(i, j)):
            a[i][j] = "2"

for i in range(150):
    for j in range(150):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(150):
    for j in range(150):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i, j)):
            a[i][j] = "4"

for i in range(1, 160):
    print(*a[i][1:160], sep="\t")
