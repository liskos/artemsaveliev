import sys, functools
sys.stdin = open("24.txt")
s = input()
s = s.replace("3", " ")
s = s.replace("4", " ")
s = s.replace("A", " ")
s = s.replace("B", " ")
s = s.replace("C", " ")
s = s.replace("D", " ")
s = s.replace("E", " ")
s = list(map(str, s.split()))

@functools.lru_cache(None)
def f(s):
    z = len(s)
    k = sum(range(1, z+1))
    for i in range(z):
        if s[i] == "0":
            k -= (z-i)
    return k


b = map(f, s)
print(sum(b))