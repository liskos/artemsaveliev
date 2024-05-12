import itertools
x = itertools.combinations([1,1,62,63,113,136,146,223], r=3)
for i in x:
    if sum(i) % 263 == 219:
        print(i, sum(i))
