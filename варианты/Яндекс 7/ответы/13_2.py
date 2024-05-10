import ipaddress

net = ipaddress.ip_network("95.112.224.0/255.255.255.128", 0)

a = []
for i in net:
    x = i.__format__("b")[-8:]
    if x == x[::-1]:
        a.append(i)
print(a)
print(len(a))
