import sys

sys.stdin = open("26.txt")

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
a = sorted(a)
b = [[a[0]]]
for i in range(1, n):
    if a[i] - b[-1][-1] <= k:
        b[-1].append(a[i])
    else:
        b.append([a[i]])
max_len = max(map(len, b))
z = [sum(x) for x in b if len(x) == max_len]
print(n - max_len, min(z))
