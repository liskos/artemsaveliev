import sys
sys.stdin = open("26.txt")

n = int(input())
k = int(input())
a = []
for i in range(n):
    x, y, z = map(int, input().split())
    if x<=1320:
        a.append([x, y-1, z])

a = sorted(a, key=lambda x:x[2])
kk = [[] for _ in range(k)]
stol = []
for x, y, t in a:

    bron = [i for i in kk[y] if x -120 <= i <= x+120]
    if not bron:
        kk[y].append(x)
        stol.append(y)
        continue
    # проверяем нужный столик, если свободен - бронируем
    # если занят проверяем с 0го и бронируем, иначе ничего
    for bb in range(k):
        bron = [i for i in kk[bb] if x-120 <= i <= x+120]
        if not bron:
            kk[bb].append(x)
            stol.append(bb)
            break
s = 0
for x in kk:
    s += len(x)
print(kk)
print(s)
print(stol[-2]+1)

