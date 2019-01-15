l, r = map(int, input().split())
if l + r == 0:
    print('Not a moose')
elif l == r:
    print('Even', l+r)
elif l != r:
    print('Odd', max(l, r)*2)
