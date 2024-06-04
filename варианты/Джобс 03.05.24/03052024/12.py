def f(s):
    while "3" in s:
        if "342" in s:
            s = s.replace("342", "4123", 1)
        if "34" in s:
            s = s.replace("34", "413", 1)
        if "32" in s:
            s = s.replace("32", "13", 1)
        if "33" in s:
            s = s.replace("33", "424", 1)
    return sum(map(int, s))


s = "3" + 40 * "4" + 25 * "2" + "3"
print(f(s))
s = "3" + "42" * 25 + 15 * "4" + "3"
print(f(s))
s = "3" + "24" * 25 + 15 * "4" + "3"
print(f(s))
s = "3" + "2" * 25 + 40 * "4" + "3"
print(f(s))
s = "3" + 20 * "424" + "2" * 5 + "3"
print(f(s))
s = "3" + "2" * 5 + 20 * "424" + "3"
print(f(s))
