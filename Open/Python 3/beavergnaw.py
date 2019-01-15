from math import pi
while True:
    D, V = map(int, input().split())
    if D + V == 0: break
    d3 = D*D*D - 6*V/pi
    d = pow(d3, 1/3.0)
    print(d)
