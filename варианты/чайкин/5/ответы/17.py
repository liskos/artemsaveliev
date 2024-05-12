def f(x):
    return int(1000 <= abs(x) <= 10000)

import sys
sys.stdin = open("17.txt")
a = [int(input()) for x in range(2700000)]
n = len(a)
k = []
for d in range(n-1):
    for i in range(n-2):
        z = [a[i], a[(i+d)%n], a[(i+2*d) % n]]
        if (f(z[0]) + f(z[1]) + f(z[2]) == 2) and (sum(z) >= 0) and (int(sum(z) ** 0.5) ** 2 == sum(z)):
            k.append(sum(z))
print(k)
print(len(k), min(k))
