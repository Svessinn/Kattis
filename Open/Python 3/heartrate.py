N = int(input())
for i in range(N):
    b, p = map(float, input().split())
    pp = 60/p
    BPM = round(b*pp, 4)
    t = 60 / p
    ABPM = round(BPM - t, 4)
    mpABPM = round(BPM + t, 4)
    print(ABPM, BPM, mpABPM)
