import ipaddress

a = []
net = ipaddress.ip_network("122.159.136.144/255.255.255.248")
for x in net:
    x1, x2, x3, x4 = str(x).split(".")
    x1, x2, x3, x4 = bin(int(x1)), bin(int(x2)), bin(int(x3)), bin(int(x4))
    if (x1.count("1") + x2.count("1") + x3.count("1") + x4.count("1")) % 4 != 0:
        a.append(1)
print(len(a))