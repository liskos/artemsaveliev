from ipaddress import *

ip1 = ip_address("123.45.32.88")
ip2 = ip_address("123.45.32.74")
ip3 = ip_address("123.45.32.95")
for i in range(24, 32):
    net = ip_network(f'{ip3}/{i}', 0)
    if ip1 in net:
        if ip2 in net:
            print(i)