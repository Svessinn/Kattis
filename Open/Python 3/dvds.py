n = int(input())
for i in range(n):
    cont = 0
    a = 1
    t = int(input())
    lst = list(map(int, input().split()))
    for j in range(t):
        if lst[j] == a:
            a += 1
        else:
            cont += 1
    print(cont)
