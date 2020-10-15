n = int(input())
n1 = n % 10
n10 = n // 10 % 10
n100 = n // 100
if n > 100 or n > 999:
    print("FALSE")
elif n1 + n10 + n100 == 13:
    print("ENTER")
else:
    print("LOCK")