l = set()
fjoldi = int(input())
for i in range(fjoldi):
    x = str(input())
    if x not in l:
        print(x)
    l.add(x)
