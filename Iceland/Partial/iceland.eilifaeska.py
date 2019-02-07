import sys
n = int(input())
j = list(map(int, sys.stdin.readline().strip().split()))
tot = sum(j)/n

if n == 1: print(-1)

elif n == 2:
  if j[0] < j[1]:
    print(1)
    print('2 1')
  elif j[1] < j[0]:
    print(1)
    print('1 2')
  elif j[1] == j[0]: print(0)
  else: print(-1)
  
elif n == 3:
  if j[0] == j[1] == j[2]: print(0)
  
elif n == 4:
  if j[0] == j[1] == j[2] == j[3]: print(0)
  else: print(-1)
