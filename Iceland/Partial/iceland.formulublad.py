n, L = map(int, input().split())
lst = []
if L == 1:
    mx = 0
    mxi = 0
    for i in range (0, n):
        l, m = map(int, input().split())
        if m > mx:
            mx = m
            mxi = i
    print(1, mx)
    print(mxi)
else:
    for i in range (0, n):
        l, m = map(int, input().split())
        lst.append([l, m])
