a = set()
for s1 in "воздух":
    for s2 in "воздух":
        for s3 in "воздух":
            for s4 in "воздух":
                for s5 in "воздух":
                    s = s1 + s2 + s3 + s4 + s5
                    if (s.count("о") + s.count("у")) == 1 and all(
                            (x not in s) for x in ["ов", "во", "ву", "ув", "хо", "ох", "ху", "ух"]):
                        a.add(s)
print(len(a))
