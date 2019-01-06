dct = {}
a = list(map(str, input().split()))
for i in a:
    if i[0] in dct:
        dct[i[0]] += 1
    else:
        dct[i[0]] = 1
print(dct[max(dct, key=(dct.get))])
