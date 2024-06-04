def f(i, j):
    return (i + 1, j), (i * 2, j), (i, j + 1), (i, j * 2)


a = [[" "] * 300 for _ in range(300)]

for i in range(300):
    for j in range(300):
        if i + j >= 123:
            a[i][j] = "0"

for i in range(123):
    for j in range(123):
        if a[i][j] == " " and any(a[x][y] == "0" for x, y in f(i, j)):
            a[i][j] = "1"

for i in range(123):
    for j in range(123):
        if a[i][j] == " " and all(a[x][y] == "1" for x, y in f(i, j)):
            a[i][j] = "2"

for i in range(123):
    for j in range(123):
        if a[i][j] == " " and any(a[x][y] == "2" for x, y in f(i, j)):
            a[i][j] = "3"

for i in range(123):
    for j in range(123):
        if a[i][j] == " " and all(a[x][y] in "13" for x, y in f(i, j)):
            a[i][j] = "4"

import sys

sys.stdout = open("19.xls", mode="x")
for i in range(1, 200):
    print(*a[i][1:200], sep="\t")
