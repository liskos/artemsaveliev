import sys

sys.stdin = open("24.txt")
s = input()
for i in "AEIOUY":
    s = s.replace(i, " ")
k = 0
for i in range(len(s) - 6):
    z = s[i:i + 7]
    if (z == z[::-1]) and (" " not in z):
        k += 1
print(k)
