import sys
sys.stdin = open("24_15339.txt")
s = input()
s = s.replace("B", "A")
s = s.replace("C", "A")
s = s.replace("7", "6")
s = s.replace("8", "6")
s = s.replace("9", "6")
t = ""
while t in s:
    t += "A6"
t = t[2:]
if t + "A" in s:
    print(t + "A", len(t)+1)
if "6" + t in s:
    print("6" + t, len(t)+1)
else:
    print(t, len(t))