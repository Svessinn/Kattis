r, d = map(int, input().split())

if(r == 1 and d ==1):
    print (0)
elif(r == 1):
    print((d - 1) * 2)
elif (d == 1):
    print((r - 1) * 2)
else:
    if(r % 2 == 0):
        print(r * d)
    elif(d % 2 == 0):
        print(r * d)
    else:
        print(r * d + 1)
