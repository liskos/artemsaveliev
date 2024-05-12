def f(a):
    for x in range(1, 1000):
        ff = (x % a == 0) or ((x % 28 != 0) or (x % 49 != 0))
        if not ff:
            return False
    return True


for a in range(1, 1000):
    if f(a):
        print(a)