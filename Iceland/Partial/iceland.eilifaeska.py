import sys
n = int(input())
l = sys.stdin.readline().strip().split()
j = []
for i in l:
  j.append(int(i))
tot = sum(j)/n

if n == 1:
  print(-1)

if n == 2:
  if j[0] < j[1]:
    print(1)
    print('2 1')
  elif j[1] < j[0]:
    print(1)
    print('1 2')
  elif j[1] == j[0]:
    print(0)
  else:
    print(-1)
