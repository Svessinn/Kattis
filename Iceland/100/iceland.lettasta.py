import sys
N = int(input())
M = int(input())
D = sys.stdin.readline().strip().split()
f = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
g = False

for i in range (0, M):
    j = [int(x) for x in sys.stdin.readline().strip().split()]
    for i in range (0, len(j)):
        f[i] += j[i]
    
for i in range (0, 12):
    if f[i] == max(f):
        print(D[i])
