sum = 0
Q = int(input())
lst = []
for i in range (0, Q):
    inp = []
    inp.append(str(input()).split())
    if inp[0][0] == 'A':
        sum += int(inp[0][1])
        lst.append(int(inp[0][1]))
    else:
        sum -= int(inp[0][1])
        lst.remove(int(inp[0][1]))
    if len(lst) != 0:
        mn = min(lst)
        mx = max(lst)
        rnd = round(sum/len(lst), 6)
    else:
        mn = mx = rnd = -1

    print(mn, mx, rnd)
