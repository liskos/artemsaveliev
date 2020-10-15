a = 157
k = 0
while a > 0:
    a //= 10
    k += 1
    for i1 in "FNS":
        a //= 10
        for i2 in "FNS":
            a //= 10
            for i3 in "FNS":
                a //= 10
                for i4 in "FNS":
                    a //= 10
                    for i5 in "FNS":
                        a //= 10
                        i = i1 + i2 + i3 + i4 + i5
print(k, i)