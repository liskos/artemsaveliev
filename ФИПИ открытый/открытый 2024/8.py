k = 0
for s1 in "апрсу":
    for s2 in "апрсу":
        for s3 in "апрсу":
            for s4 in "апрсу":
                for s5 in "апрсу":
                    s = s1+s2+s3+s4+s5
                    k += 1
                    if (s.count("у") <= 1) and ("аа" not in s):
                        print(k, s)
