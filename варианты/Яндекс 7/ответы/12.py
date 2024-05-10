def f(s):
    while ("8858" in s) or ("555" in s):
        if "8858" in s:
            s = s.replace("8858", "4", 1)
        else:
            s = s.replace("555", "58", 1)
        if "5858" in s:
            s = s.replace("5858", "85", 1)
    return sum(int(x) for x in s)


for n in range(4, 10000):
    s = "8" + n * "5"
    if f(s) == 66:
        print(n)
