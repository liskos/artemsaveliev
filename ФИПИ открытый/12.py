n = "8"*82
while n.find("1111") != -1 or n.find("8888") != -1:
    if n.find("1111") != -1: n = n.replace("1111", "8", 1)
    else: n = n.replace("8888", "11", 1)
print(n)