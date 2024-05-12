from fnmatch import fnmatch
a = []
lst = []
for i in range(1, 10**10//98591 + 1):
    x = i * 98591
    if fnmatch(str(x), "5?2*3?3?"):
        a.append(x)
        lst.append(x / 98591)
a.sort()
lst.sort()
print(a)
print(lst)