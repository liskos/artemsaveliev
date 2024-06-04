def f(n):
    ch = bin(n)[2:]
    if n % 2 == 0: ch += "01"
    else: ch = "1" + ch + "1"
    return int(ch, 2)

print(f(12), f(5))
for i in range(1, 1000):
    if f(i) > 156:
        print(i)
        break