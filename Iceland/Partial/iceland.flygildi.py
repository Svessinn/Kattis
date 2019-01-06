import math

lengd = [0.0]

fjoldi = int(input())

for i in range(fjoldi):
    x, y = map(float, input().split())
    length = math.sqrt((x*x)+(y*y))
    lengd.append(length)

endiTilByrjun = math.sqrt((lengd[0]**2)+(max(lengd)**2))
lengd.append(endiTilByrjun)

summa = sum(lengd)
print(summa)
