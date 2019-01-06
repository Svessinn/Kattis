N, K = map(int, input().split())
order = list(map(int, input().split()))
lst = [i for i in range(1, N+1)]

for j in range (0, K):
    lst = [lst[i-1] for i in order]
print(*lst, sep = ' ')
