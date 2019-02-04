K = int(input())
start = 'A'
new = ''
for i in range(K):
    for j in (start):
        if j == 'A':
            new += 'B'
        elif j == 'B':
            new += 'BA'
    start = new
    new = ''
    
print(start.count('A'), start.count('B'))
