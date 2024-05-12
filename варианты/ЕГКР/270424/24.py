import sys
sys.stdin = open("24.txt")
s = input()
k = ""
while k in s:
    k += "KLMN"
while k not in s:
    k = k[:-1]
k = "KLMN" + k
while k not in s:
    k = k[1:]
print(len(k))
