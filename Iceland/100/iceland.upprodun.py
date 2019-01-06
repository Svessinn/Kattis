n = int(input())
m = int(input())
d = m

for x in range(n,0,-1):
    print('*' * int(d/x))
    d = d - (d//x)
