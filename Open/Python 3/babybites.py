k = int(input())
lst = list(map(str, input().split()))
tot = 0
for i in range(1, k + 1):
    if lst[i-1] == 'mumble' or int(lst[i-1]) == i:
        tot += 1
print('makes sense' if k == tot else 'something is fishy')
