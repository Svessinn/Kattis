H, M = map(int, input().split())
minu = M - 45
if minu < 0:
    H -= 1
    if H < 0:
        H = 23
    Min = 60 + minu
    print(H, Min)

else: print(H, minu)
