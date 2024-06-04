from ipaddress import *

lst = []
net = ip_network("105.224.200.224/255.255.255.224")
for x in net:
    s = list(map(bin, map(int, str(x).split("."))))
    l = ""
    for i in s:
        l += i
    if l.count("1") % 4 == 0:
        lst.append(x)
print(len(lst))