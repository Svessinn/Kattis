for i in range (0, int(input())):
    r, e, c = map(int, input().split())
    if (r + c) > e:
        print('do not advertise')
    if (r + c) < e:
        print('advertise')
    if (r + c) == e:
        print('does not matter')
