def delit(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return a


for i in range(397438, 443520 + 1, 2):
    x = delit(i)
    c = [j for j in x if j % 2 == 0]
    if len(c) >= 142:
        print(len(c), max(c), sep="\t")
