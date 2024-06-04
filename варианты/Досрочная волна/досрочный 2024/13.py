import ipaddress

net = ipaddress.ip_network("105.224.200.224/255.255.255.224")
a = []
for ip in net:
    if ip.__format__("b").count("1") % 4 == 0:
        a.append(ip)
print(len(a))
