f = False
for j in str(input()).strip().split(' EDA '):
    true = set()
    false = set()
    for i in j.strip('()').split(' OG '):
        if i[0] == '!':
            false.add(i[1:])
        else:
            true.add(i)

    if len(true & false) == 0:
        f = True
if f:
    print('Jebb')
else:
    print('Neibb')
