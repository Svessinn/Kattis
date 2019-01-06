mx = [1, 1, 2, 2, 2, 8]
now = list(map(int, input().split()))
new = []
for i in range(0, 6):
    new.append(mx[i]-now[i])
print(*new, sep = ' ')
