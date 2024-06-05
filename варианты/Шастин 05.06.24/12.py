for i in range(4, 10000):
    n = "5" + "4"*i
    while "54" in n or "4444" in n or "7744" in n:
        if "54" in n:
            n = n.replace("54", "77", 1)
        if "4444" in n:
            n = n.replace("4444", "5", 1)
        if "7744" in n:
            n = n.replace("7744", "45", 1)
    if int(sum(map(int, n))**0.5)**2 == sum(map(int, n)):
        print(i, sum(map(int, n))**0.5)
        break