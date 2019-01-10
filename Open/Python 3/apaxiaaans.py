a = str(input())
b = a[0]
last = b[0]
for i in range(1, len(a)):
    if a[i] != last:
        b += a[i]
        last = b[len(b)-1]
print(b)
