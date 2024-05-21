k = 0
for s1 in "2468":
    for s2 in "012345678":
        for s3 in "012345678":
            for s4 in "012345678":
                for s5 in "012345678":
                    for s6 in "012345678":
                        for s7 in "124578":
                            s = s1 + s2 + s3 + s4 + s5 + s6 + s7
                            if s.count("6") >= 1:
                                k += 1
print(k)
