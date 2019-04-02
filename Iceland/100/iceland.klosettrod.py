dct = {}
n = int(input())
l = list(map(int, input().split()))
for i in range(len(l)):
    dct[i+1] = l[i]

sl = sorted(dct.items(), key=lambda x: x[1])

for i in range(len(sl)-1, -1, -1):
    print(sl[i][0], end=' ')
