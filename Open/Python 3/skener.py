R, C, ZR, ZC = map(int, input().split())
for i in range(R):
    r = str(input())
    for j in range(ZR):
        print(''.join([c*ZC for c in r]))
