a = set()
b = ["000", "111", "222", "333", "444", "555", "666", "777"]
for s1 in "1234567":
    for s2 in "01234567":
        for s3 in "01234567":
            for s4 in "01234567":
                for s5 in "01234567":
                    s = s1 + s2 + s3 + s4 + s5
                    if len(set(s)) == 3 and any(i in s for i in b):
                        a.add(s)
print(len(a))

