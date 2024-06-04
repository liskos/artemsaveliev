import sys

sys.stdin = open("26.txt")

n = int(input())
a = [int(input()) for _ in range(n)]
a = sorted(a, reverse=True)
b = [a[0]]  # Отобранные коржи
razn = 8
c = [x for x in a if x <= b[-1] - razn]  # те коржи которые можно поместить
while c:
    b.append(c[0])
    c = [x for x in a if x <= b[-1] - razn]
print(len(b), b[-1])
