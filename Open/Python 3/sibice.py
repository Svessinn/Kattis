import math
N, W, H = map(int, input().split())
maxsize = math.sqrt(W**2 + H**2)
for i in range (0, N):
    if int(input()) <= maxsize:
        print('DA')
    else:
        print('NE')
