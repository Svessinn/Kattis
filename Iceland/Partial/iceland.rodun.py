import sys, random
n,k = [int(x) for x in sys.stdin.readline().strip().split()]
nem = {}
nem2 = {}
for i in sys.stdin.readline().strip().split():
  nem[i] = 0

for i in range(0,k):
  a,check,b = sys.stdin.readline().strip().split()
  if check == ">":
    nem[a] += 1
    nem[b] -= 1
  elif check == "<":
    nem[a] -= 1
    nem[b] += 1
sortedd = sorted(nem.values())

for k,v in nem.items():
  nem2[v + random.uniform(0, 0.000000000001)] = k

nem3 = []
for i in (sorted(nem2.items())):
  nem3.append(i[1])

print(" ".join(nem3))
