n = 2 * 729**2014 + 2 * 243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2 * 9**2020 - 2024
lst = []
while n > 0:
    lst.append(n % 27)
    n //= 27
a = []
for x in lst:
    if x > 9:
        a.append(x)
print(len(a))