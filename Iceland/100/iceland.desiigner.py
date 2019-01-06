import sys

n = str(sys.stdin.readline())
if n is not None:
    n = n.strip()

serhlodar = ['a','e', 'i', 'o', 'u', 'y']

if n != '':
    fyrsti = n[0]
    seinasti = n[-1]
    if len(n) <= 3 or len(n) == 0:
        print ('Neibb')
    else:
        for i in range(1, len(n) - 2):
            if n[i] != 'r':
                failed = True
                break
        else:
            failed = False
    
        if fyrsti == 'b' and failed != True and seinasti in serhlodar:
            print ('Jebb')
        else:
            print ('Neibb')
else:
    print('Neibb')
