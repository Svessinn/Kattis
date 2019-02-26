import sys

N = int(input())
cur = 0
cnt = 0
bits = list(map(int, sys.stdin.readline().split()))
cnt = sum(bits)
for i in range(len(bits)):
    bits[i] = -1 if bits[i] == 1 else 1

mx = -1
for i in range (N):
    cur = max(bits[i], cur + bits[i])
    mx = max(mx, cur)
print(mx + cnt)
