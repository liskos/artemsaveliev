import sys

sys.stdin = open("24.txt")

s = input()
s = s.replace("T", " ")
s = s.replace("U", " ")
s = s.replace("V", " ")
s = s.replace("W", " ")

t = ""
m = 0
for i in range(0, len(s) - 1, 2):
    if s[i] == s[i + 1] and t == "":
        t = s[i] + s[i + 1]
    elif s[i] == s[i + 1] and t[-1] != s[i]:
        t += s[i] + s[i + 1]
    elif s[i] == s[i + 1] and t[-1] == s[i]:
        t = s[i] + s[i + 1]
    else:
        t = ""
    m = max(m, len(t))

for i in range(1, len(s) - 1, 2):
    if s[i] == s[i + 1] and t == "":
        t = s[i] + s[i + 1]
    elif s[i] == s[i + 1] and t[-1] != s[i]:
        t += s[i] + s[i + 1]
    elif s[i] == s[i + 1] and t[-1] == s[i]:
        t = s[i] + s[i + 1]
    else:
        t = ""
    m = max(m, len(t))
print(m)
