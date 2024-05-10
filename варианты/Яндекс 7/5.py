def sem(n):
    ch = ""
    while n > 0:
        ch += str(n % 7)
        n //= 7
    return ch[::-1]

def f(n):
    ch = sem(n)
    if n % 7 == 0: ch = ch + ch[-2:]
    else: ch = ch + sem((n % 7)*2)
    return int(ch, 7)

lst = []
for i in range(1, 500):
    if f(i) < 220:
        lst.append(i)
print(max(lst))
