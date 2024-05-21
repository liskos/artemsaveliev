def f(a ,b):
    if a == b: return 1
    if a > b: return 0
    if a == 13: return 0
    return f(a + 2, b) + f(a * 3, b) + f(a*a, b)

print(f(3, 49))