T = int(input())
while T > 0:
    lst = list(map(str, input().split()))
    while True:
        w = str(input())
        if w == 'what does the fox say?':
            print(*lst, sep = ' ')
            T -= 1
            break
        else:
            w = w.split()
            c = lst.count(w[2])
            for i in range(c):
                lst.remove(w[2])
