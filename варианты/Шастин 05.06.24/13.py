from ipaddress import *

for i in range(1, 110):
    net = ip_network(f"217.109.{i}.94/255.255.254.0", 0)
    b = True
    for x in net:
        if x.packed[0].__format__("b").count("0")+x.packed[1].__format__("b").count("0")>x.packed[2].__format__("b").count("0")+x.packed[3].__format__("b").count("0"):
            b = False
    if b:
        print(i)