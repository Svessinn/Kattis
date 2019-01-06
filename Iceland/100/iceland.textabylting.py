import sys

N = int(sys.stdin.readline())

lst = []

max_len = 0
min_len = 90000
for i in range(0,N):
    lst.append(sys.stdin.readline()[:-1])

for i in range(0,len(lst)):
    if (len(lst[i]) > max_len):
        max_len = len(lst[i])
    if (len(lst[i]) < min_len):
        min_len = len(lst[i])

for i in range(0,max_len):
    for item in lst:
        if (i < len(item)):
            sys.stdout.write(item[i])
        else:
            sys.stdout.write(" ")
    if i < max_len-1:
        print("")
