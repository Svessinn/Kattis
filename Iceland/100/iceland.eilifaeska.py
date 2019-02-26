import sys
n = int(input())
j = list(map(int, sys.stdin.readline().strip().split()))
tot = sum(j)/n

if n == 1:
  print(0)

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
  mxi, mni, midi = 0, 0, 0
  for i in range(n):
    if j[i] > j[mxi]: mxi = i
  for i in range(n):
    if j[i] < j[mni]: mni = i
  for i in range(n):
    if i != mxi and i != mni: midi = i
  
  if 2*j[midi] == j[mni] + j[mxi]:
    print(1)
    print(mxi+1, mni+1)
  elif j[0] == j[1] == j[2]: print(0)
  else: print(-1)
  
elif n == 4:
  js = [j[0], j[1], j[2], j[3]]
  lst = list()
  for i in range(len(js)):
    lst.append((js[i], i+1))
  lst.sort()
  if lst[0][0] == lst[1][0] and lst[2][0] == lst[3][0]:
    print(2)
    print(lst[3][1], lst[1][1])
    print(lst[2][1], lst[0][1])
  elif lst[0][0] != lst[1][0] != lst[2][0] != lst[3][0]:
    print(4)
    print(lst[3][1], lst[2][1])
    print(lst[1][1], lst[0][1])
    print(lst[3][1], lst[1][1])
    print(lst[2][1], lst[0][1])
  else:
    print(-1)
