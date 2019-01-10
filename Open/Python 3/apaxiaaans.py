c = str(input())
new = ''
for i in range(len(c)):
    if c[i] != c[i-1]:
        new += c[i]
print(new)
