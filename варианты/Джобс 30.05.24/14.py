def f(n, b):
    s = ""
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]

for i in range(1, 1000000):
    if f(i, 7)[-1] == "3" and f(i, 5)[-1] == "2" and len(f(i, 7)) <= 5 and len(f(i, 5)) <= 6:
        print(i)