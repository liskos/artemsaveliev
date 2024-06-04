for x in range(27):
    s1 = int("123024", 27) + x * 27 ** 2
    s2 = int("135078", 27) + x * 27 ** 2
    s = s1 + s2
    if s % 26 == 0:
        print(x, s // 26)
