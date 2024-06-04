def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += "01"
    else:
        b = "1" + b + "1"
    return int(b, 2)


print(f(12), f(5))
for i in range(1, 1000):
    if f(i) > 156:
        print(i)
        break
