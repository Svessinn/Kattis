def check(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


for p in range(10000000000000000):
    dct = {}
    x = int(input())
    if x != 0:
        for i in range(x):
            inp = list(map(str, input().split()))
            l = len(inp)-1
            li = str(inp[l])
            lis = li.lower()
            if lis in dct:
                dct[lis] += 1
            else:
                dct[lis] = 1
        print("List %d:"% (p+1))
        for i, j in sorted(dct.items()):
            print(i,'|', j)
    else:
        exit()
