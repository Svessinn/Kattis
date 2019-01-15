denied = 0
tot = 0
L, x = map(int, input().split())
for i in range (x):
    el, p = map(str, input().split())
    p = int(p)
    if el == 'enter':
        if tot + p <= L:
            tot += p
        else:
            denied += 1
    else:
        tot -= p
print(denied)
