def f(i, j):
    return (i + 2, j), (i, j + 2), (i + 6, j), (i, j + 6), (i * 3, j), (i, j * 3)


a = [[" "] * 1000 for _ in range(1000)]

for i in range(1000):
    for j in range(1000):
        if (i + j) / 2 >= 144:
            a[i][j] = "0"

for i in range(290):
    for j in range(290):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in f(i, j)):
            a[i][j] = "1"

for i in range(290):
    for j in range(290):
        if a[i][j] == " " and all(a[x][y] == "1" for x, y in f(i, j)):
            a[i][j] = "2"

for i in range(290):
    for j in range(290):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(290):
    for j in range(290):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i, j)):
            a[i][j] = "4"

for i in range(1, 300):
    print(*a[i][1:300], sep="\t")
