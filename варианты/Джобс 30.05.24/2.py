print("a b c d")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = (a or b) and ((not b) == c) and (d or not a)
                if not f:
                    print(a, b, c, d)