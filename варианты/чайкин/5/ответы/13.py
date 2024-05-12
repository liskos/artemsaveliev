import ipaddress

ip1 = ipaddress.ip_address("92.149.25.164")
ip2 = ipaddress.ip_address("92.149.37.2")

for n in range(16, 31):
    net1 = ipaddress.ip_network(f"{ip1}/{n}", 0)
    if ip1 in net1.hosts() and ip2 in net1.hosts():
        print(n, net1.netmask, sum(map(int, str(net1.netmask).split("."))))