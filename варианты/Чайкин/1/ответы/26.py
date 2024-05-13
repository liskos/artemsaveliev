import sys
sys.stdin = open("26.txt")

n = int(input())
a = [int(input()) for _ in range(n)]
s = 0
m = 0
for i in range(len(a)-2):
    for j in range(i+1, len(a)-1):
        z = 0
        l = 0
        s12 = a[i] + a[j]
        for k in a[j+1:]:
            if k < s12:
                z += 1
                m = max(m, s12 + l)
        s += z
print(s, m)
