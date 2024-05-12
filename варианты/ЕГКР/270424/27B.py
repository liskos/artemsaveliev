import sys
sys.stdin = open("27_B.txt")

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
print(b[113], b[146], b[223])
print(s -376-672-223)
print(n-3)
