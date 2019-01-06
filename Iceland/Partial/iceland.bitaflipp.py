import sys

n = int(input())
bits = (sys.stdin.readline().split())

mx = 0
for i in range (0, n):
    for j in range (i, n):
        cur = 0
        for k in range (0, n):
            if (i <= k and k <= j):
                cur += 1 - int(bits[k])
            else:
                cur += int(bits[k])
        mx = max(mx, cur)
print(mx)
