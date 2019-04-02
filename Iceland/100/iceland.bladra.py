k, q = map(int, input().split())
dct = { i+1:0 for i in range(k) }
for i in range(q):
    a, b = map(int, input().split())
    dct[b] += 1


print(min(dct.values()))
