##def check(a, b):
##    return len(set(a).intersection(b))
##while True:
##    jack, jill = map(int, input().split())
##    ja = []
##    ji = []
##    if jack == 0 and jill == 0:
##        break
##    else:
##        for i in range(jack):
##            ja.append(int(input()))
##        for i in range(jill):
##            ji.append(int(input()))
##        print(check(ja, ji))
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    a = set(int(input()) for _ in range(n))
    ans = 0
    for _ in range(m):
        if int(input()) in a:
            ans += 1
    print(ans)
