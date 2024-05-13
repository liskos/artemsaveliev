from ipaddress import ip_network

def de(n):
    a = set()
    for i in range(1, n+1):
        if n % i == 0: a.add(i)
    return a

lst = []
net = ip_network("172.118.1.255/255.255.252.0", 0)
for x in net.hosts():
    a = list(map(bin, map(int, list(str(x).split(".")))))
    s = ""
    for i in a:
        s += i
    if len(de(s.count("1"))) == 2:
        lst.append(x)
print(len(lst))