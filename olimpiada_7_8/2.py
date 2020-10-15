k = 0
for i1 in "FNS":
    k += 1
    for i2 in "FNS":
        k += 1
        for i3 in "FNS":
             k += 1
             for i4 in "FNS":
                k += 1
                for i5 in "FNS":
                    k += 1
                    i = i1 + i2 + i3 + i4 + i5
                    print(k, i)