lst = []
for i in range(4, 1000):
    n = "5" + "2"*i
    while "52" in n or "222" in n or "122" in n:
        if "52" in n:
            n = n.replace("52", "11", 1)
        if "222" in n:
            n = n.replace("222", "15", 1)
        if "122" in n:
            n = n.replace("122", "21", 1)
    a = []
    for x in n:
        a.append(int(x))
    if str(sum(a)**0.5 % 2) in "1.0 0.0":
        lst.append(i)
print(max(lst))