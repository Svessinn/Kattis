N, Q = map(int, input().split())
companies = list(map(int, input().split()))
for i in range(Q):
    z, C, X = map(int, input().split())
    if z == 1:
        companies[C-1] = X
    if z == 2:
        print(abs(companies[C-1] - companies[X-1]))
