n = 5 * 3**1917 + 6 * 2**1878 + 7 * 3**1870 - 1991
lst = []
while n > 0:
    lst.append(n % 17)
    n //= 17
mx = 0
for i in range(1, 17):
    if lst.count(i) > mx:
        mx = lst.count(i)
        mxi = lst.index(i)
print(lst[mxi])