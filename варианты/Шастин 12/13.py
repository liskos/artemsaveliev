from ipaddress import *

lst = []
net = ip_network("192.168.72.128/255.255.255.128")
for x in net:
    if x.__format__("b").count("1") % 10 == 0:
        lst.append(x)
print(len(lst))