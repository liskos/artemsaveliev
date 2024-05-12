g = [0]
for i in range(1, 77555533+1):
    if int(i ** 0.5) ** 2 == i:
        g.append(g[-1]-i)
    else:
        g.append(g[-1]+i)

print(g[77555533]% (10**7))