N, K = map(int, input().split())
order = list(map(int, input().split()))

def dunno(a, b):
    return [a[b[i]-1] for i in range(len(a))]

def ath(o, k):
    if k == 0:
        return list(range(1, len(o)+1))
    elif k % 2 == 1:
        return dunno(o, ath(o, k-1))
    else:
        res = ath(o, k//2)
        return dunno(res, res)

print(' '.join(map(str, ath(order, K))))
