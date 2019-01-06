dct = {}
for i in range (0, int(input())):
    npt = str(input())
    lst = npt.split()
    if lst[0] == 'INNTAK':
        dct[lst[1]] = lst[2] == 'SATT'
    elif lst[0] == 'OG':
        dct[lst[3]] = dct[lst[1]] and dct[lst[2]]
    elif lst[0] == 'EDA':
        dct[lst[3]] = dct[lst[1]] or dct[lst[2]]
    elif lst[0] == 'EKKI':
        dct[lst[2]] = not dct[lst[1]]
    elif lst[0] == 'UTTAK':
        print (lst[1], 'SATT' if dct[lst[1]] else 'OSATT')
