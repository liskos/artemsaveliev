lst = [179]
for i in range(9000, 10000):
    a = []
    n = "8" + "5"*i
    while n.find("8858") != -1 or n.find("555") != -1:
        if n.find("8858") != -1:
            n = n.replace("8858", "4", 1)
        if n.find("5858") != -1:
            n = n.replace("5858", "85", 1)
        else:
            n = n.replace("555", "58", 1)
    for z in n:
        a.append(int(z))
    if sum(a) == 66:
        lst.append(i)
print(max(lst))