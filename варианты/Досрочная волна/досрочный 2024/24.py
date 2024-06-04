import sys

sys.stdin = open("24.txt")

s = input()
s = s.replace("B", "A")
s = s.replace("C", "A")
s = s.replace("7", "6")
s = s.replace("8", "6")
s = s.replace("9", "6")
t = s[-1]
m = 0
for i in s[1:]:
    if i != t[-1]:
        t += i
        m = max(m, len(t))
    else:
        t = i
print(m)
