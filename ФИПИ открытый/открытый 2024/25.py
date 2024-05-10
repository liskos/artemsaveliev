import fnmatch
for i in range(5216, 5216484+1):
    x = str(i * 1917)
    if fnmatch.fnmatch(x, "3?12?14*5"):
        print(x, i, sep="\t")
