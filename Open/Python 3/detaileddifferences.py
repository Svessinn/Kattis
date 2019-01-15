for i in range(int(input())):
    a = str(input())
    b = str(input())
    lst = ''
    for j in range(len(a)):
        if a[j] == b[j]:
            lst += '.'
        else:
            lst += '*'
    print(a)
    print(b)
    print(lst)
    print()
