n = input()
n1 = int(n)
s = sum(map(int, n))
k = 0
x = 0
while n1 > 0:
    n1 //= 10
    k += 1
for i in range(0, 100000):
    x += 1
    if s % k == 0 and str(x) == n:
        print(i + s)
        break
    if int(n) < 11:
        print(n)
        break
    if s % k == 1 and str(x) == n:
        print(i + s)
        break