def sumdel(n):
    s = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sum(s)


def isprost(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def delit(x):
    for i in range(2, x):
        if x % i == 0:
            return x // i


a = [int(f"13{x}9") for x in "0123456789"]
for i in range(1, 10 ** 6):
    a.extend([int(f"1{i}3{x}9") for x in "0123456789"])
for i in a:
    if int(i ** 0.5) ** 2 == i and isprost(sumdel(i)):
        print(i, delit(i))
