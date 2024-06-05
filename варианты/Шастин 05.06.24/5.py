def s(n):
    k = 0
    for i in n:
        k += int(i)
    return k

def tr(n):
    s = ""
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]

def f(n):
    ch = tr(n)
    if s(ch) % 3 == 0: ch += "212"
    else: ch += tr(s(ch)*2)
    return int(ch, 3)

print(f(11), f(12))
lst = []
for i in range(1000):
    if f(i) > 490:
        lst.append(f(i))
print(min(lst))