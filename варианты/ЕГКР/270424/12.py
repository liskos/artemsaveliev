def f(s):
    while ("11" in s) or ("444" in s) or ("8888" in s):
        if "11" in s:
            s = s.replace("11", "4", 1)
        if "444" in s:
            s = s.replace("444", "88", 1)
        if "8888" in s:
            s = s.replace("8888", "1", 1)
    return s

a = []
for n in range(4, 10000):
    s = "8" + n * "4"
    a.append(sum(map(int , f(s))))
print(max(a))