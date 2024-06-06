from fnmatch import *

for i in range(1, 10**12//86513 + 1):
    x = str(i * 86513)
    if fnmatch(x, "17*46??8") and int(sum(map(int, x))**0.5)**2 == sum(map(int, x)):
        print(x, int(x)//86513, sep="\t")