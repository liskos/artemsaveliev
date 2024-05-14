a = set()
k = 0
for s1 in "ЕИКРСУЯ":
    for s2 in "ЕИКРСУЯ":
        for s3 in "ЕИКРСУЯ":
            for s4 in "ЕИКРСУЯ":
                for s5 in "ЕИКРСУЯ":
                    for s6 in "ЕИКРСУЯ":
                        k += 1
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if k % 2 == 0 and s1 != "К" and s.count("Е") + s.count("У") + s.count("И") + s.count("Я") <= 2:
                            a.add(s)
print(len(a))
