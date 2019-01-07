N, K = map(int, input().split())
order = list(map(int, input().split()))

def ath(o, k):
    if k == 0:
        return list(range(1, len(o)+1))
    elif k % 2 == 1:
        return [o[ath(o, k-1)[i]-1] for i in range(len(o))]
    else:
        res = ath(o, k//2)
        return [res[res[i]-1] for i in range(len(o))]

print(' '.join(map(str, ath(order, K))))
