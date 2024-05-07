import sys
sys.stdin = open("24.txt")
s = input()
s = s.replace("R", "Q")
s = s.replace("W", "Q")
s = s.replace("2", "1")
s = s.replace("4", "1")
t = s[0]
m = 0
for i in s:
    if t[-1] != i:
        t += i
        m = max(m, len(t))
    else:
        t = i
print(m)
print("Q1"*8 + "Q" in s)
print("1" + "Q1"*8 in s)
print("Q1" * 9 in s)