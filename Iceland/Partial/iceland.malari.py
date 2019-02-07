N, M = map(int,input().split())
s = set()
for _ in range(M):
    i, j = map(int,input().split())
    for it in range(i, j+1):
        if it not in s:
            s.add(it)

print(len(s))

if len(s) > N//2:
    print('The Mexicans took our jobs! Sad!')
else:
    print('The Mexicans are Lazy! Sad!')
