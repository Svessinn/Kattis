dct = {}
N, Q = map(int, input().split())
companies = list(map(int, input().split()))
for i in range(N):
    dct[i+1] = companies[i]
for i in range(Q):
    z, C, X = map(int, input().split())
    if z == 1:
        dct[C] = X
        Vals = list(dct.values())
    #print(dct)
    if z == 2:
        #print(Vals)
        print(abs(Vals[C-1] - Vals[X-1]))
