import sys

sys.stdin = open("26.txt")

n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([i + 1, x, y])
b = []  # массив деталей с начала ленты транспортера
c = []  # массив деталей с конца ленты
k = 0
while a:
    min1 = min(a, key=lambda x: x[1])
    min2 = min(a, key=lambda x: x[2])
    if min1[1] < min2[2]:
        b.append(min1)
        k = min1
        a.pop(a.index(min1))
    else:
        c.append(min2)
        k = min2
        a.pop(a.index(min2))
d = b + c[::-1]
k2 = len(d[:d.index(k)])
print(k[0], k2)
