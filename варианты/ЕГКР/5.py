def f(n):
    ch = bin(n)[2:]
    if n % 3 == 0: ch += ch[-2:]
    else: ch += bin((n % 3)*3)[2:]
    return int(ch, 2)

print(f(9), f(10))
for i in range(300):
    if f(i) >= 195:
        print(f(i))
        break