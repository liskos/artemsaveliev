import sys

sys.stdin = open("24.txt")
s = input()

t = ""
m = 0
for i in s:
    t += i
    while "AHAHA" in t:
        t = t[1:]
    m = max(m, len(t))
print(m)
