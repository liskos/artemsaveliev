def pr(n):
    s = ""
    while n > 0:
        s += str(n % 4)
        n //= 4
    return s[::-1]

def f(n):
    ch = pr(n)
    if n % 3 == 0: ch = ch[-1] + ch[1:-2] + ch[0] + "1"
    else: ch = ch + str(n % 3)
    return int(ch, 4)

a = []
for i in range(1, 1000):
    if f(i) <= 340:
        a.append(f(i))
print(max(a))