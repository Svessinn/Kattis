import sys
from queue import PriorityQueue
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    inp = sys.stdin.readline().split()
    lst.append((int(inp[0]), 1, int(inp[1])))

bolir = sys.stdin.readline().split()
lst1 = []
for i in range(N):
    x = int(bolir[i])
    lst1.append((x, 2, 0))

lst2 = []
lst2.extend(lst1)
lst2.extend(lst)
lst2.sort()
queue = PriorityQueue()

def check():
    for i in range(len(lst2)):
        if lst2[i][1] == 1:
            queue.put(lst2[i][2])
            continue
        if not queue.empty():
            chk = queue.get()
            if chk < lst2[i][0]:
                return False
        else:
            return False
print(check())
if check() == None: print('Jebb')
else: print('Neibb')
