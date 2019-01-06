tot = 0
for i in range(0, int(input())):
    x = int(input())
    y = str(x)[-1:]
    x = str(x)[:-1]
    tot += int(x)**int(y)
print(tot)
