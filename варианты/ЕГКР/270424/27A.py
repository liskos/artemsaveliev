import sys
sys.stdin = open("27_A_.txt")

n = int(input())
a = [int(input()) for _ in range(n)]

s = sum(a)
print(s, s % 263)
b = [[] for _ in range(263)]
for x in a:
    b[x % 263].append(x)
for i in range(263):
    if len(b[i]) > 0:
        print(i , len(b[i]))
print(b[241], b[1])
print(s-1293-1-1)
print(n-3)
