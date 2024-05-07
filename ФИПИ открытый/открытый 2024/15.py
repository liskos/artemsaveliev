def alg(a):
    for x in range(1, 1000):
        f = (x % a == 0) or ((x % 14 != 0) or (x % 4 != 0))
        if not f:
            return False
    return True


for a in range(1, 1000):
    if alg(a):
        print(a)