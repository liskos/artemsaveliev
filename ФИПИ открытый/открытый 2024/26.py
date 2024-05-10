import sys
sys.stdin = open("26.txt")

n = int(input())
a = [int(input()) for _ in range(n)]

a = sorted(a, reverse=True)
print(n)
print(a)

b = [a[0]]
c = [x for x in a if x <= b[-1]-4]
while len(c) > 0:
    b.append(c[0])
    c = [x for x in a if x <= b[-1]-4]
print(b)
print(len(b),b[-1])