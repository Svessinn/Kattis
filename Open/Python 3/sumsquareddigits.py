def ssd(num, b, n):
    ans = 0
    while b > 0:
        v = b % n
        ans  += v ** 2
        b //= n
    print(num, ans)

for i in range(int(input())):
    num, n1, n2 = map(int, input().split())
    ssd(num, n2, n1)
