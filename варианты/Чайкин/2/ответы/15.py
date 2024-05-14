def f(a):
    for x in range(1, 10000):
        ff = (x % a == 0) or not ((x % 17 == 0) and (x % 23 == 0))
        if not ff:
            return False
    return True


for a in range(1, 10000):
    if f(a):
        print(a)
