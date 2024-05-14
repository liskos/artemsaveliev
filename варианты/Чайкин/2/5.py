def su(n):
    sm = 0
    for i in str(n):
        sm += int(i)
    return sm

def mx(n):
    a = []
    for i in str(n):
        a.append(int(i))
    return str(max(a))

def f(n):
    s = oct(n)[2:]
    if su(n) % 2 == 0: s += str(n % 3)
    else: s = mx(int(s)) + s
    return int(s, 8)

print(f(6), f(5))
for i in range(500):
    if f(i) > 127:
        print(i)
        break