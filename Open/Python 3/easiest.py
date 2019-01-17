def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

while True:
    N = int(input())
    if N == 0:
        break
    p = 11
    while True:
        if sum_digits(N) == sum_digits(N*p):
            print(p)
            break
        else:
            p += 1
