import sys
sys.stdin = open("27_A.txt")

n = int(input())
a = [int(input()) for _ in range(n)]
s = 0
x = []
for i in range(n):
    for k in range(1, (n+1)//2):
        s += a[(i - k) % n] * k + a[(i + k) % n] * k
    if n % 2 == 0:
        s += a[(i-n//2) % n] * (n//2)
    x.append(s)
    s = 0
print(x)
print(min(x))
