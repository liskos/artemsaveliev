def f(n):
    s = 0
    p = 1
    for i in str(n):
        s += int(i)
        p *= int(i)
    return str(s) + str(p)

print(f(2135))
for i in range(1000000):
    if f(i) == "3522050":
        print(i)
        break