lst = (str(input()).split(';'))
tot = 0
for i in lst:
    if '-' in i:
        k = i.split('-')
        x = int(k[0])
        y = int(k[1])
        for j in range(x, y+1):
            tot += 1
    else: tot += 1
print(tot)
