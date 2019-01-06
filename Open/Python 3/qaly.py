tot = 0
for i in range(0, int(input())):
    x, y = map(float, input().split())
    tot += (x*y)
print(tot)
