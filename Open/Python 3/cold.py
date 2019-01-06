input()
tot = 0
x = list(map(int, input().split()))
for i in x:
    if i < 0:
        tot+= 1
print(tot)
