import fnmatch
for i in range(1, 10**10//98591 + 1):
    x = i * 98591
    if fnmatch.fnmatch(str(x), "5?2*3?3?"):
        print(x, i,sep="\t")
