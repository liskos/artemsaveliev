import sys
sys.stdin = open("24_9960.txt")
s = input()
alf = [i for i in "BCDFGHJKLMNPQRSTVWXZ"]
lst = []
for i in range(len(alf)):
    for j in range(len(alf)):
        for y in range(len(alf)):
            for z in range(len(alf)):
                t = alf[i] + alf[j] + alf[y] + alf[z] + alf[y] + alf[j] + alf[i]
                if t in s:
                    lst.append(t)
print(len(lst))