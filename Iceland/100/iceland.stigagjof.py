import sys

daemi =  str(input())
n = int(input())
haedsta = 0


for i in range (0, n):
  a, d, s = sys.stdin.readline().strip().split()
  if d == daemi:
    if int(s) > haedsta:
      haedsta = int(s)
print(haedsta)
