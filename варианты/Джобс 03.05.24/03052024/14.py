for x in "0123456789abcdefghijk":
    for y in "0123456789abcdefghijk":
        s = int(f"943697{x}21", 21) - int(f"2{y}9253", 21)
        if s % 20 == 0:
            print(int(x, 21) - int(y, 21), s // 20)
