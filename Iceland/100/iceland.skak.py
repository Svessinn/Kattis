xh, yh = map(int, input().split())
xp, yp = map(int, input().split())
if xh == xp and yh == yp: print(0)
if xh == xp and yh != yp or xh != xp and yh == yp: print(1)
else: print(2)