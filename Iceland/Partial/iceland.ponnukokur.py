n, q = map(int, input().split())
dct = {}
def flip(dct, m):
    if dct[m] == 0:
        dct.update({m: 1})
    else:
        dct.update({m: 0})
        
def count(dct, l, n):
    x = 0
    for i in range(l, n):
        m = i + 1
        if dct[m] == 1:
            x += 1
    print(x)
    
for i in range(1, n+1):
    dct[i] = 0

for i in range(q):
    lst = (str(input()).split())
    if lst[0] == '1':
        m = int(lst[1])
        flip(dct, m)
    elif lst[0] == '2':
        for i in range(0, n):
            m = i + 1
            flip(dct, m)
    elif lst[0] == '3':
        count(dct, 0, n)
    else:
        l = int(lst[1])
        r = int(lst[2])
        count(dct, l, r)
