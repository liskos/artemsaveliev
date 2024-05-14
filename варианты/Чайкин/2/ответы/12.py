def f(s):
    while ("25" in s) or ("355" in s) or ("555" in s):
        if "25" in s:
            s = s.replace("25", "32", 1)
        if "355" in s:
            s = s.replace("355", "25", 1)
        if "555" in s:
            s = s.replace("555", "3", 1)
    return s


def prost():
    a = [2]
    for i in range(3, 1000):
        for x in a:
            if i % x == 0:
                break
        else:
            a.append(i)
    return a


a = []
p = prost()
for i in range(4, 1000):
    s = "3" + "5" * i
    if sum(int(x) for x in f(s)) in p:
        a.append(i)
print(len(a))
