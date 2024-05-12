def f(s):
    while ("!1" in s) or ("!2" in s) or ("!0" in s):
        if "!1" in s:
            s = s.replace("!1", "2!", 1)
        if "!2" in s:
            s = s.replace("!2", "30!", 1)
        if "!0" in s:
            s = s.replace("!0", "1!", 1)
    s = s.replace("0", "5", 1)
    return s


for n in range(10):
    s = "!" + "0"*15 + "1" * n + 19 * "2"
    print(n, f(s), sum(map(int, f(s).replace("!",""))))

for n in range(0,10,2):
    x = 77 + n
    for i in range(1, int(x**0.5)):
        print(x, x-i*i, int((x-i*i)**0.5)**2 == x - i*i)