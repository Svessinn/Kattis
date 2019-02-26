import collections

simanumer = []
Counter = collections.Counter()
n = int(input())
for i in range (n):
    x = str(input())
    simanumer.append(x)
    for j in range(len(x)+1):
        Counter[x[:j]] += 1

n = int(input())
for i in range (n):
    x = str(input())
    result = Counter[x]
    print (result)
