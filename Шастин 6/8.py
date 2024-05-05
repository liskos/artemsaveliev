k = 0
for i in range(10000, 100000):
    n = oct(i)[2:]
    bol = False
    for z in range(10):
        if str(z)*3 in n and n.count(str(z)) != 4 and n.count(str(z)) != 5:
            bol = True
    if bol:
        k += 1
print(k)