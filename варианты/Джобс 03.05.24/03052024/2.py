print("a b c d | f")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = (not a or b) and (not b or not c) and (c or d)
                if f:
                    print(a, b, c, d, "|", int(f))
