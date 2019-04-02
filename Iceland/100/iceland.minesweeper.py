h, b, n = map(int, input().split())
lst = []
for i in range(h):
    lst.append(['.' for _ in range(b)])
for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    lst[x][y] = '*'

for i in lst:
    print(*i, sep='')
