def f(a, b):
    if a == b: return 1
    if a < b: return 0
    if a == 32: return 0
    return f(a-2, b) + f(a-5, b) + f(a//3, b)

print(f(46, 19) * f(19, 7))
