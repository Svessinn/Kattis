N, M = map(int,input().split())
lst = []
for _ in range(M):
    i, j = map(int, input().split())
    lst.append((i-1, -1))
    lst.append((j, 1))
lst.append((N, -2))
lst.sort()

d = 0
sm = 0
last = 0
for i in range(len(lst)):
    if d > 0:
        sm += lst[i][0] - last
    if lst[i][1] == -2: break
    d -= lst[i][1]
    last = lst[i][0]

print(sm)
if sm > N//2:
    print('The Mexicans took our jobs! Sad!')
else:
    print('The Mexicans are Lazy! Sad!')
