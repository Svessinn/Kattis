par = [0]
sz = [1]

def uf_find(a):
    if par[a] == a: return a
    else:
        par[a] = uf_find(par[a])
        return par[a]

def uf_union(a, b):
    pa = uf_find(a)
    pb = uf_find(b)
    if pa != pb:
        par[pb] = uf_find(a)
        sz[pa] += sz[pb]
        return True
    else:
        return False

def uf_size(a):
    return sz[uf_find(a)]

def main():
    n, q = map(int, input().split())

    for i in range(1, n+1):
        par.append(i)
        sz.append(1)

    for i in range(q):
        op = list(map(int, input().split()))

        if op[0] == 1:
            a, b = op[1], op[2]
            uf_union(a, b)
        else:
            a = op[1]
            print(uf_size(a)-1)

main()
