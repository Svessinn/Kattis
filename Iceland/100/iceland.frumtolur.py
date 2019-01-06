def frumtala(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True

for i in range (1,542):
    if frumtala(i):
        print (i)
