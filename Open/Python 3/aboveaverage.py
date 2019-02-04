def prettyfloat(y):
    return "%0.3f" % y
lst1 = []
for i in range(int(input())):
    x = list(map(int, input().split()))
    lst = []
    avg = 0
    tot = 0
    for j in range(1, len(x)):
        tot += x[j]
        lst.append(x[j])
    avg = tot / x[0]
    tot1 = 0
    for j in range(len(x)-1):
        if lst[j] > avg:
            tot1 += 1
    percent = round((tot1 / x[0] * 100), 3)
    print(str(prettyfloat(percent))+'%')
