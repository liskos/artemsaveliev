def f(n):
    x = 1
    if n > 1:
        x += f(n - 2)
        x += f(n // 2)
        x += 1
    x += 1
    return x


print(f(127))
