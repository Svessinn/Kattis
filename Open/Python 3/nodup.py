lst = list(map(str, input().split()))
dct = {}
for i in lst:
    if i not in dct:
        dct[i] = 1
    else:
        print('no')
        exit()
print('yes')
