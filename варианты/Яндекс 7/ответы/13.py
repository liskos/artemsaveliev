import ipaddress

net = ipaddress.ip_network("95.112.224.0/255.255.255.128")
print(net)
a = []
for i in net:
    s1, s2, s3, s4 = str(i).split(".")
    s4 = bin(int(s4))[2:].zfill(8)
    if s4 == s4[::-1]:
        a.append(str(i))
print(a)
print(len(a))
