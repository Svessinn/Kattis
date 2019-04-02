n, r, c = map(int, input().split())
lst = []
for i in range(r):
    lst.append(list(map(str, input().split())))
    
for _ in range(n//c):
    l = []
    for i in range(c):
        l.append(str(input()))
    if l == lst[_]: print('left')
    else: print('right')
