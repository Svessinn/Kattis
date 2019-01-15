N = int(input())
for i in range(N):
    lst = list(map(int, input().split()))
    nb = 0
    for j in range(len(lst) - 1):
        if lst[j+1] == 0:
            break
        elif lst[j+1] > lst[j] * 2:
            nb += lst[j]*2 - lst[j + 1]
    print(abs(nb))
