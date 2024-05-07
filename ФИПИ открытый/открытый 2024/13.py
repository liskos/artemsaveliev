import ipaddress

net = ipaddress.ip_network("122.159.136.144/255.255.255.248")

for s in net:
    z = "".join(bin(int(x))[2:] for x in str(s).split("."))
    if z.count("1") % 4 != 0:
        print(z, z.count("1"))

