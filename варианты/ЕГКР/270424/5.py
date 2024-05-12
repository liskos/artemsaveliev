def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + b[-2:]
    else:
        b = b + bin(n % 3*3)[2:]
    return int(b, 2)


a = []
for i in range(1, 1000):
    if f(i) >= 195:
        a.append(f(i))
print(min(a))
