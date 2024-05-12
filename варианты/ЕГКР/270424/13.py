import ipaddress
net = ipaddress.ip_network("112.208.0.0/255.255.128.0")
k = 0
for ip in net:
    if ip.__format__("b").count("1") % 11 == 0:
        k += 1
print(k)