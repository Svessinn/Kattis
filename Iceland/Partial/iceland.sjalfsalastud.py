import sys

C, n10, n50, n100 = [int(x) for x in sys.stdin.readline().strip().split()]

verd = C*80
myntir = 0

#print(C, n10, n50, n100)

while C > 0:
  if n100 > 0:
    n100 -= 1
    n10 += 2
    C -= 1
    myntir += 1
  elif n50 > 0 and n10 >= 3:
    if n50 >= 2:
      n50 -= 2
      n10 += 2
      C -= 1
      myntir += 2
    elif n50 < 2:
      n50 -= 1
      n10 -= 3
      C-= 1
      myntir += 4
  else:
    n10 -= 8
    C -= 1
    myntir += 8

print(myntir)
