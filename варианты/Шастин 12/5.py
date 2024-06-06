def che(n):
    s = ""
    while n > 0:
        s += str(n % 4)
        n //= 4
    return s[::-1]

def f(n):
    ch = che(n)
    if n % 4 == 0: ch += ch[:2]
    if n % 4 != 0: ch += che(n % 4 * 4)
    return int(ch, 4)

lst = []
print(f(11), f(12))
for i in range(1, 1000):
    if f(i) > 291:
        lst.append(f(i))
print(min(lst))