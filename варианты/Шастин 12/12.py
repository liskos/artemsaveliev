for i in range(4, 10000):
    n = "9" + "6"*i
    while "96" in n or "6666" in n or "1166" in n:
        n = n.replace("96", "11", 1)
        n = n.replace("6666", "9", 1)
        n = n.replace("1166", "69", 1)
    if sum(map(int, n)) % 37 == 0:
        print(i)
        break