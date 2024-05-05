for p in range(31, 38):
    n1 = 17 + 29 * p
    n2 = 26 + 23 * p
    n3 = 7 + 21 * p + p**2
    if n1 + n2 + 30 == n3:
        print(p)