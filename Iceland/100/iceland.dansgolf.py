N, M, K = map(int,input().split())
s = set()
for i in range(K):
    x, y = map(int,input().split())
    s.add(x - y)
print(len(s))
