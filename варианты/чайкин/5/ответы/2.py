for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x or not y) and (x != z) and w
                g = (not x or y) and (not y or z) and (not z or w)
                print(x, y ,z, w , "|", int(f), int(g))
