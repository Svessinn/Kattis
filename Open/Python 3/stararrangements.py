n = int(input())
print(str(n) + ':')
for i in range(2, n):
    #print(i)
    for j in range(max(1, i-1), i+1):
        #print(j)
        a = n//i
        for k in range(1, a+1):
            #print(k)
            left = n - k*i
            if left % j != 0:
                continue
            b = left // j
            if k == b or k == b+1:
                print(str(i)+','+str(j))
