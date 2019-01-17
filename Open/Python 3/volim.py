time = 0
player = int(input())
K = int(input())
for i in range(K):
    T, Z = map(str, input().split())
    T = int(T)
    time += T
    if time >= 210:
        print(player)
        break
    else:
        if Z == 'T':
            if player == 8:
                player = 1
            else:
                player += 1
