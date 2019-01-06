import sys

n = int(sys.stdin.readline().strip())
N = int(n/3)
x = sys.stdin.readline().strip().split()
m = []
for i in x:
    m.append(int(i))
m.sort()
#print(m)
idx = 0

lst = []
for i in range(0,3):
    if i == 0:
        for item in m[N:N*2]:
            lst.append(item)
    elif i == 1:
        for item in m[:N]:
            lst.append(item)
    else:
        for item in m[N*2:]:
            lst.append(item)

for item in lst:
    if idx != n:
        sys.stdout.write(str(item)+" ")
    else:
        sys.stdout.write(str(item))
