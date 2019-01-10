N, B = map(str, input().split())
N = int(N)
tot = 0
for i in range(4*N):
    inp = str(input())
    if inp[0] == '7' or inp[0] == '8' or inp[0] == '9' and inp[1] != B:
        tot += 0
    elif inp[0] == 'T':
        tot += 10
    elif inp[0] == '9' and inp[1] == B:
        tot += 14
    elif inp[0] == 'Q':
        tot += 3
    elif inp[0] == 'K':
        tot += 4
    elif inp[0] == 'A':
        tot += 11
    elif inp[0] == 'J':
        if inp[1] == B:
            tot += 20
        else:
            tot += 2
print(tot)
