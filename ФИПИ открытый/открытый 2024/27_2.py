import sys
sys.stdin = open("27_B.txt")

n = int(input())
a = [int(input()) for _ in range(n)]
a_c = [a[0]]
a_l = a[1:(n+1)//2]
a_r = a[(n+1)//2:]
a_r = a_r[::-1]
s = []
s_l = [(i+1)*a_l[i] for i in range(len(a_l))]
s_r = [(i+1)*a_r[i] for i in range(len(a_r))]
s.append(sum(s_l)+sum(s_r))
i = 1
s_ = -sum(a[i: n//2 + i])+sum(a[n//2+i:]+a[:i])
s.append(s[-1]+s_)
for i in range(1, n-1):
    s_ = s_ + a[i % n] * 2 - a[(n // 2 + i) % n] * 2
    s.append(s[-1]+s_)
print(min(s))
