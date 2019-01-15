t = int(input())
for i in range(t):
    n = int(input())
    stores = list(map(int, input().split()))
    print((max(stores) - min(stores)) * 2)
