skip = []
sprengjur = []
n = int(input())

def chk1(a, b, m, i, j):
    if (a[0][0] - b[0][0]) ** 2 + (a[0][1] - b[0][1]) ** 2 + (a[0][2] - b[0][2]) ** 2 <= (a[1] + b[1]) ** 2:
        lst[j].append(m + i)

def chk2(a, b, m, i, j):
    if (a[0][0] - b[j][0][0]) ** 2 + (a[0][1] - b[j][0][1]) ** 2 + (a[0][2] - b[j][0][2]) ** 2 <= (2 * a[1] + b[j][1]) ** 2:
        lst[m + i].append(m + j)
    if (a[0][0] - b[j][0][0]) ** 2 + (a[0][1] - b[j][0][1]) ** 2 + (a[0][2] - b[j][0][2]) ** 2 <= (2 * b[j][1] + a[1]) ** 2:
        lst[m + j].append(m + i)

def tot(a):
    return sum(1 for i in range(n) if m + i not in a)

for i in range(0, n):
    x, y, z, r = [int(_) for _ in input().split()]
    skip.append(((x, y, z), r))

m = int(input())
for i in range(0, m):
    x, y, z, r = [int(_) for _ in input().split()]
    sprengjur.append(((x, y, z), r))

lst = [[] for _ in range(n + m)]
for i, sk in enumerate(skip):
    for j, sp in enumerate(sprengjur):
        chk1(sk, sp, m, i, j)
    for j in range(i):
        chk2(sk, skip, m, i, j)

marked = set()
for i in range(m):
    st = [i]
    while st:
        j = st.pop()
        marked.add(j)
        for k in lst[j]:
            if k not in marked:
                st.append(k)
print(tot(marked))
