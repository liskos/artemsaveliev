import ipaddress

for i in range(24, 15, -1):
    net = ipaddress.ip_network(f"238.51.1.202/{i}", strict=False)
    k = True
    for z in net:
        s1, s2, s3, s4 = str(z).split(".")
        if bin(int(s1)).count("1") + bin(int(s2)).count("1") < bin(int(s3)).count("1") + bin(int(s4)).count("1"):
            k = False
    if k:
        print(i)
print(22-8-8)
print(int("11111100",2))