def main():
    n = int()
    k = int()
    n, k = map(int, input().strip().split())
    x = 1
    y = 1
    mxh = n + 1
    mnb = 1
    mnh = 1
    if (k == 1):
        print(n+1, n+1)
        print(1, 1)
    while(x+y*k <= n+1):
        y *= k
        x += y
        mnh += 1
    mxb = int()
    if(x == n+1):
        mxb = y
    else:
        mnh += 1
        l = n-(x-1)
        m = l//k
        o = l%k
        mxb = y + m*(k-1) +max(0, o - 1)
    print(mnh, mxh)
    print(mnb, mxb)
main()
