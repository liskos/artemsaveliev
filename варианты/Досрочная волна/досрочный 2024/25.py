import fnmatch

for i in range(1, 10 ** 10 // 2024):
    x = i * 2024
    if fnmatch.fnmatch(str(x), "1*2322?2"):
        print(x, i)
