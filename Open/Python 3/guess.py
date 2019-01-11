import sys
mn = 0
mx = 1001
ans = ''
for i in range(10):
    guess = (mx + mn)//2
    print(guess)
    sys.stdout.flush()
    ans = str(input())
    if ans == 'correct':
        break
    if ans == 'lower':
        mx = guess 
    elif ans == 'higher':
        mn = guess
