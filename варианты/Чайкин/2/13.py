from ipaddress import ip_network
net = ip_network("49.26.38.163/255.255.255.224", 0)
lst = []
for x in net.hosts():
    a = list(str(x).split("."))
    if int(a[3]) % 2 != 0:
        lst.append(1)
print(len(lst))