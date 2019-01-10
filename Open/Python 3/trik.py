inp = str(input())
fin = 1
for i in inp:
    if i == 'A':
        if fin == 1:
            fin += 1
        elif fin == 2:
            fin -= 1
    elif i == 'B':
        if fin == 2:
            fin += 1
        elif fin == 3:
            fin -= 1
    elif i == 'C':
        if fin == 1:
            fin += 2
        elif fin == 3:
            fin -= 2
print(fin)
