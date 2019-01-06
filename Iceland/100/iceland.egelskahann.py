def check(n):
    if n == 1:
        return 1
    res = 0
    if n % 2 == 0:
        res = 2*check(n//2)-1
    else:
        res = 2*check(n//2)+1
    return res
print(check(int(input())))
