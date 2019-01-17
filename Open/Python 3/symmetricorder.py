three = [0, 2, 1]
four = [0, 2, 3, 1]
five = [0, 2, 4, 3, 1]
six = [0, 2, 4, 5, 3, 1]
seven = [0, 2, 4, 6, 5, 3, 1]
eight = [0, 2, 4, 6, 7, 6 ,4, 1]
nine = [0, 2, 4, 6, 8, 7, 5, 3, 1]
ten = [0, 2, 4, 6, 8, 9, 7, 5, 3, 1]
eleven = [0, 2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
twelve = [0, 2, 4, 6, 8, 10, 11, 9, 7, 5, 3, 1]
thirteen = [0, 2, 4, 6, 8, 10, 12, 11, 9, 7, 5, 3, 1]
fourteen = [0, 2, 4, 6, 8, 10, 12, 13, 11, 9, 7, 5, 3, 1]
fifteen = [0, 2, 4, 6, 8, 10, 12, 14, 13, 11, 9, 7, 5, 3, 1]
j = 1
while True:
    names = []
    n = int(input())
    if n == 0: break
    print('SET', j)
    for i in range(n): names.append(str(input()))
    if n == 1 or n == 2:
        for i in range(n): print(names[i])
    elif n == 3:
        for i in range(n): print(names[three[i]])
    elif n == 4:
        for i in range(n): print(names[four[i]])
    elif n == 5:
        for i in range(n): print(names[five[i]])
    elif n == 6:
        for i in range(n): print(names[six[i]])
    elif n == 7:
        for i in range(n): print(names[seven[i]])
    elif n == 8:
        for i in range(n): print(names[eight[i]])
    elif n == 9:
        for i in range(n): print(names[nine[i]])
    elif n == 10:
        for i in range(n): print(names[ten[i]])
    elif n == 11:
        for i in range(n): print(names[eleven[i]])
    elif n == 12:
        for i in range(n): print(names[twelve[i]])
    elif n == 13:
        for i in range(n): print(names[thirteen[i]])
    elif n == 14:
        for i in range(n): print(names[fourteen[i]])
    elif n == 15:
        for i in range(n): print(names[fifteen[i]])
    j += 1
