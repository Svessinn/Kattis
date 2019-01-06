n = int(input())
l = {}
for x in range (0, n):
    name = input()
    place = input()
    if(place in l):
        l[place] = l[place]+1
    else:
        l[place] = 1

for item, value in l.items():
    print(item+" "+str(value))
