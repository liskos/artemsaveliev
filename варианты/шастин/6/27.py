import sys
sys.stdin = open("27A.txt")

n = int(input())
a = [int(input()) for _ in range(n)]
rez = {0:0}  # сумма и длина цепочки
for i in a:  # Элементы числа
    b = rez.copy()
    for j in rez:  # суммы на предыдущем шаге
        if j+i in rez:
            b[j+i] = max(b[j] +1, b[i+j])
        else:
            b[i+j] = b[j]+1
    rez = b.copy()
print(rez[0])
