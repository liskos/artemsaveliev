import sys
sys.stdin = open("26.txt")

s, n = map(int, input().split())
a = [int(input()) for _ in range(n)]
a = sorted(a)  # сортируем по возрастанию
b = [] # погруженные посылки
c = [] # непоместившиеся посылки
v = 0 # погруженный объем в грузовике
for i in range(n):
    if v + a[i] <= s: # если эта посылка влезает в свободное место грузовика
        b.append(a[i])
        v += a[i]
    else:
        c.append(a[i])
print(len(b))
x = (s - v) + b[-1] # оставшееся место + место последней посылки
d = [j for j in c+[b[-1]] if j <= x] # посылки которые могут поместиться на х размер
print(max(d))