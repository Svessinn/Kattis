S, N = map(int, input().split())
k = list(map(str, input().split()))
for h in range(0, N):
    score = 0
    name = str(input())
    k1 = list(map(str, input().split()))
    for i in range(0, len(k)):
        if k[i] == k1[i]:
            score += 1
    fin = round(((score/S)*10)*2)/2
    print(name + ': ' + str(fin))
