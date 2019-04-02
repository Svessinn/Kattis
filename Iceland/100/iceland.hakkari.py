h, b= map(int, input().split())
lst = []
count = 0
for j in range(h):
    s = str(input())
    for i in range(len(s)):
        if s[i] == '*':
            count += 1
            lst.append([j+1, i+1])

print(count)
for i in lst:
    print(*i, sep=' ')
