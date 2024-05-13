import ipaddress

net = ipaddress.ip_network("172.118.0.0/255.255.252.0")
a = list(net)
a.pop(0)
a.pop(-1)
z = []
for i in a:
    s1, s2, s3, s4 = map(int, str(i).split("."))
    x = bin(s1).count("1") + bin(s2).count("1") + bin(s3).count("1") + bin(s4).count("1")
    if x in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        z.append(i)
print(len(z))
