for x in "0123456789abcdefgh":
    s = int(f"973f8{x}24", 18) + int(f"7241{x}1e5", 18) + int(f"31{x}154c", 18)
    if s % 11 == 0:
        print(s // 11)
