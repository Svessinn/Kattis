tot = 0
N = int(input())
lst = list(map(int, input().split()))
for i in lst:
    if i >= 0:
        tot += i
    else:
        N -= 1
print(tot/N)
