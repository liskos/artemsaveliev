from ipaddress import *
lst = []
net = ip_network("95.112.224.0/255.255.255.128")
for x in net:
    x1, x2, x3, x4 = str(x).split(".")
    x4 = bin(int(x4))[2:]
    if x4 == x4[::-1]:
        lst.append(x)
print(len(lst))