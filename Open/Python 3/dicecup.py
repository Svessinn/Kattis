n, m = map(int, input().split())
dct = {}
for i in range(1, n+1):
    for j in range(1, m+1):
        if (i+j) in dct:
            dct[i+j] += 1
        else:
            dct[i+j] = 1

mxv = max(dct.values())
mxk = [k for k, v in dct.items() if v == mxv]
for i in mxk:
    print(i)

