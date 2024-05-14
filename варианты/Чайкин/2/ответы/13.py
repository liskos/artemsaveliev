import ipaddress

net = ipaddress.ip_network("49.26.38.160/255.255.255.224")
net = list(map(str, net))
net.pop(0)
net.pop(-1)
z = []
for i in net:
    a1, a2, a3, a4 = i.split(".")
    b = bin(int(a4))[5:]
    z.append(int(b, 2))
x = [i for i in z if i % 2 == 0]
print(len(x))
