import ipaddress

for i in range(24, 16, -1):
    net = ipaddress.ip_network(f"238.51.0.0/{i}")
    a = []
    for x in net:
        x1, x2, x3, x4 = str(x).split(".")
        x1, x2, x3, x4 = bin(int(x1)), bin(int(x2)), bin(int(x3)), bin(int(x4))
        if x1.count("1") + x2.count("1") >= x3.count("1") + x4.count("1"):
            a.append(1)
    if len(a) == len(list(net)):
        print(i)



