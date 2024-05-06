def f(n):
    ch = bin(n)[2:]
    if n % 2 == 0: return int("10" + ch, 2)
    else: return int("1" + ch + "01", 2)

print(f(4), f(5))
for i in range(500):
    if f(i) > 516:
        print(i)
        break