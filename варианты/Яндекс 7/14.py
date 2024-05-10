n = 7 * 49**120 - 6 * 343**65 - 5 * 7**40
lst = []
while n > 0:
    lst.append(n % 7)
    n //= 7
print(lst.count(6))