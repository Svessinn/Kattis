def check(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

dct = {}

for i in range(int(input())):
    x, y = map(str, input().split())
    if check(x):
        dct[y] = int(x)/2
    else:
        dct[x] = int(y)
#print(dct)
srtdDct = sorted(dct.items(), key= lambda kv: kv[1])
#print(srtdDct)
for i in range(len(srtdDct)):
    print(srtdDct[i][0])
