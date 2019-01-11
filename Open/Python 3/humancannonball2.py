from math import cos, sin, radians
n = int(input())
for _ in range(n):
    velos, angle, x, h1, h2 = map(float, input().split())
    r = radians(angle)
    t = x / (velos * cos(r))
    y = (velos * t * sin(r)) - (0.5 * (9.81)*t*t)
    if h1 + 1 <= y <= h2 - 1: print('Safe')
    else: print('Not Safe')
