def f(i, j):
    return (i+1,j), (i*2,j),(i,j+1),(i,j*2)


a = [[" "] * 200 for _ in range(200)]

for i in range(200):
    for j in range(200):
        if i + j >= 59:
            a[i][j] = "0"

for i in range(59):
    for j in range(59):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in f(i, j)):
            a[i][j] = "1"

for i in range(59):
    for j in range(59):
        if a[i][j] == " " and all(a[x][y] == "1" for x, y in f(i, j)):
            a[i][j] = "2"

for i in range(59):
    for j in range(59):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(59):
    for j in range(59):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i, j)):
            a[i][j] = "4"

for i in range(1, 200):
    print(*a[i][1:], sep="\t")
