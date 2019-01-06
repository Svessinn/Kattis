import math

C = int(input())

def athuga(tala):
    return (tala * math.log(tala) / math.log(10) / 10**6) <= C

minst = 1
haedst = 1
while athuga(haedst):
    haedst *= 2

utkoma = 0
while minst <= haedst:
    mid = (minst+haedst)//2
    if athuga(mid):
        utkoma = mid
        minst = mid + 1
    else:
        haedst = mid - 1

print(utkoma)
