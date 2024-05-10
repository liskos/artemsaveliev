def f(x, y, A):
    return ((x >= A) or (121 >= x*x)) and ((y*y < 49) or (A < y))

for A in range(700):
    if all(f(x, y, A) == True for x in range(700) for y in range(700)):
        print(A)