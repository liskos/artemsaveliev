a = []
for i in range(4, 10000):
    n = "8" + "7"*i
    while n.find("57") != -1 or n.find("877") != -1 or n.find("777") != -1:
        if n.find("57") != -1:
            n = n.replace("57", "7", 1)
        if n.find("877") != -1:
            n = n.replace("877", "75", 1)
        if n.find("777") != -1:
            n = n.replace("777", "8", 1)
    z = 1
    for x in n:
        z *= int(x)
    a.append(z)
print(max(a))