X, Y = map(int, input().split())
xy = 4*X + 3*Y
if xy % 2 == 1: print('impossible')
else: print('possible')
