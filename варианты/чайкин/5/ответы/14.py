def f(n, i):
    t = "0123456789"
    s = ""
    while n > 0:
        s = t[n % i] + s
        n = n // i
    return s

def palindrom(s):
    k = 0
    for i in {x for x in s}:
        if s.count(i) % 2 == 1:
            k += 1
    return ((k == 1) and (len(s) % 2 == 1)) or ((k == 0) and (len(s) % 2 == 0))

k = 0
for i in range(15, 7**7, 16):
    if (len(f(i, 7)) <= 7) and (i % 16 == 15) and palindrom(f(i,5)):
        k += 1
print(k)
