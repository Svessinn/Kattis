import sys
import math
N = int(sys.stdin.readline().strip())
lengd = []
for i in range(N):
    x,y = map(int , sys.stdin.readline().strip().split())
    lengd.append(math.sqrt(x**2+y**2))

N = int(sys.stdin.readline().strip())

count = 0
#print(lengd)
for i in range(N):
    check = int(sys.stdin.readline().strip())
    count = 0
    for x in lengd:
        #print(check)
        #print(sys.stdin.readline().strip(),math.floor(x))
        if check > math.floor(x):
            count += 1
    print(count)
