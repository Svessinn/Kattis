X = int(input())
N = int(input())
g = X
for i in range(N):
    j = int(input())
    g += X
    g -= j
print(g)
