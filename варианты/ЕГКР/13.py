from ipaddress import ip_network

j = []
net = ip_network("112.208.0.0/255.255.128.0")
for x in net:
    lst = list(str(x).split("."))
    a = list(map(bin, map(int, lst)))
    s = ""
    for x in a:
        s += x[2:]
    if s.count("1") % 11 == 0:
        j.append(x)
print(len(j))