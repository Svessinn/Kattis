simanumer = []
res = []
for i in range (0, int(input())):
    simanumer.append(str(input()))

for i in range (0, int(input())):
    x = str(input())
    result = [y for y in simanumer if x in y[0:len(x)]]
    print (len(result))
