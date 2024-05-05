import fnmatch
for i in range(1, 10**10//2024 + 1):
    x = i * 2024
    if fnmatch.fnmatch(str(x), "112?57*4") and sum(map(int, str(x))) % 2 == 1:
        print(x, i, sep="\t")
