print("x z w y")
for x in 0, 1:
    for z in 0, 1:
        for w in 0, 1:
            for y in 0, 1:
                 f = (x or ((not z) and w) or w) == (y and (not x) and w)
                 if f:
                     print(x, z, w, y)