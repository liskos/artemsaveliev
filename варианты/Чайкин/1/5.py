def tr(n):
    s = ""
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]

def f(n):
    ch = tr(n)
    if n % 4 == 0: ch += ch[-3:]
    else: ch += tr((n % 4) * 4)
    return int(ch, 3)

lst = []
for i in range(1, 1000):
    if f(i) < 127:
        lst.append(f(i))
print(max(lst))