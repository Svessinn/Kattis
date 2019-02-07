import sys
r = int(sys.stdin.readline())
tot = 0
x = 0
y = r

while x < r:
    while y*y + x*x > r*r:
            y -= 1
    tot += y
    x += 1

tot *= 4
tot += 1
print(tot)
