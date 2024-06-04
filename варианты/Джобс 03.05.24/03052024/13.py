import ipaddress

ip1 = ipaddress.ip_address("123.20.103.136")
ip2 = ipaddress.ip_address("123.20.103.151")
for x in range(24, 32):
    net = ipaddress.ip_network(f"{ip1}/{x}", 0)
    if ip2 in net:
        print(x, "одна сеть")
    else:
        print(x, "разные", net.netmask, bin(net.netmask.packed[3]))
print(bin(ip1.packed[3]))
print(bin(ip2.packed[3]))
