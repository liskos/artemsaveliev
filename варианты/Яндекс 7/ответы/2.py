print("x y u w | F")
for x in 0, 1:
    for y in 0, 1:
        for u in 0, 1:
            for w in 0, 1:
                f = (not ((not y or w) == x)) and u
                print(x, y, u, w, "|", int(f))
