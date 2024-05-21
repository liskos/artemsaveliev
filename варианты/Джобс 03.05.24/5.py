def tr(n):
    s = ""
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]

def f(n):
    ch = tr(n)
    if n % 2 == 0: ch = "2" + ch + tr(int(ch[-1])*2)
    else: ch = tr(int(ch[0])*2) + ch + "2"
    return int(ch, 3)

lst = []
for i in range(1, 500):
    if f(i) > 100:
        lst.append(f(i))
print(min(lst))
