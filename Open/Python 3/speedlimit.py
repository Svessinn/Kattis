j = True
while j:
    tot = 0
    time = 0
    c = int(input())
    if c != -1:
        for i in range(0, c):
            x, y = map(int, input().split())
            tot += x*(y-time)
            time = y
        print(tot, 'miles')
    else:
        j = False
