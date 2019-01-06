from collections import Counter
import sys

N, K = map(int, sys.stdin.readline().split())
count = Counter()
for i in range(N):
    S = int(sys.stdin.readline())
    count[S] += 1

found = False
for i in count:
    need = 2 if 2 * i == K else 1
    if count[i] >= need and count[K - i] >= need:
        print(i, K - i)
        found = True
        break
if not found:
    print('Neibb')
