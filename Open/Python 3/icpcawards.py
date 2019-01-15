dct = {}
N = int(input())
for i in range(N):
    Uni, Team = map(str, input().split())
    if len(dct) != 12:
        if Uni not in dct:
            dct[Uni] = Team
    else: break
for (k, v) in dct.items():
    print(k, v)
