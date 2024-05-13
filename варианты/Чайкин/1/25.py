from fnmatch import fnmatch
lst = [[]]
for i in range(1, 10**9//1024 + 1):
    x = i * 1024
    if fnmatch(str(x), "3?5?21*4?"):
        lst[0].append(x)
        lst.append(x // 1024)
for i in range(len(lst)-1):
    print(lst[0][i], lst[i+1], sep="\t")