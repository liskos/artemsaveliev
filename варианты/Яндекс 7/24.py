import sys
sys.stdin = open("24.txt")
s = input()
lst = []
while s.find("AHAHA") != -1:
    lst.append(len(s[:s.find("AHAHA")]))
    s = s[s.find("AHAHA"):]
    s = s.removeprefix("AHAHA")
print(max(lst))