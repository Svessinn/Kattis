N = int(input())
for i in range(N):
    s = set()
    G = int(input())
    C = list(map(int, input().split()))
    for j in range(G):
        chk = C[j]
        if chk in s:
            s.remove(chk)
        else:
            s.add(chk)
    print('Case #'+str(i+1)+':', end=' ')
    print(*s, sep=' ')
