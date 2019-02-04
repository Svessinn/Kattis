N = int(input())
for i in range(N):
    x, y, res = map(int, input().split())
    if x + y == res or x - y == res or x / y == res or x * y == res or y / x == res or y - x == res:
        print('Possible')
    else:
        print('Impossible')
