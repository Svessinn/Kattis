inp = str(input())
upper = 0
lower = 0
ws = 0
sym = 0
tot = len(inp)
for i in inp:
    if i.isupper(): upper += 1
    elif i.islower(): lower += 1
    elif i == '_': ws += 1
    else: sym += 1
print(ws/tot)
print(lower/tot)
print(upper/tot)
print(sym/tot)
