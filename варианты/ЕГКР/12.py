lst = []
for i in range(4, 10000):
    n = "8" + "4"*i
    while "11" in n or "444" in n or "8888" in n:
        if "11" in n:
            n = n.replace("11", "4", 1)
        if "444" in n:
            n = n.replace("444", "88", 1)
        if "8888" in n:
            n = n.replace("8888", "1", 1)
    a = []
    for x in n:
        a.append(int(x))
    lst.append(sum(a))
print(max(lst))