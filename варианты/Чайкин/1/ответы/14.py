x = 5 * 3 ** 1917 + 6 * 2 ** 1878 + 7 * 3 ** 1870 - 1991
s = [0] * 17
while x > 0:
    s[x % 17] += 1
    x = x // 17
for i, j in enumerate(s):
    if max(s) == j:
        print(i, j, "<-- max")
    else:
        print(i, j)
