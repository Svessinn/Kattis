tot = 0
C = float(input())
for i in range(0, int(input())):
    w, l = map(float, input().split())
    tot += (w*l)
tot *= C
print(tot)
