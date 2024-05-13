import sys

sys.stdin = open("24_10131.txt")
s = input()
ka = 0
kb = 0
a = []
for i in s:
    if i == "A":
        ka += 1
    elif i == "B":
        kb += 1
    a.append(ka - kb)
b = a[::-1]
z = []
l = len(a)
for i in range(min(a), max(a)):
    z.append(l - (a.index(i) + b.index(i)))
print(max(z))
