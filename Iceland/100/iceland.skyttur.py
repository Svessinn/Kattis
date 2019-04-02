n = int(input())
x = str(input())
y = str(input())
new = ''
for i in range(len(x)):
    if x[i] == '0' and y[i] == '0': new += '0'
    elif x[i] == '0' and y[i] == '1': new += '1'
    elif x[i] == '1' and y[i] == '0': new += '1'
    elif x[i] == '1' and y[i] == '1': new += '0'
print(new)
