alf = list("q w e r t y u i o p a s d f g h j k l z x c v b n m 0 1 2 3 4 5 6 7 8 9".split(" "))
alf.sort()
for x in alf[:22]:
    if (int(f"56{x}c20", 22) + int(f"89f{x}2", 22) + int(f"h24{x}k21", 22)) % 21 == 0:
        print((int(f"56{x}c20", 22) + int(f"89f{x}2", 22) + int(f"h24{x}k21", 22)) // 21)
        break