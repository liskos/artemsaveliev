import sys
sys.stdin = open("24_17102.txt")
s = input()
t = ""
mx = 0
for i in range(0, len(s)-2, 2):
    t += s[i]+s[i+1]
    if t[-2]+t[-1] in "XMNFEO":
        mx = max(len(t), mx)
    else:
        t = ""
print(mx)