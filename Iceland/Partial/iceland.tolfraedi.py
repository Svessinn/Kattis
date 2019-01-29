import sys
sum = 0
Q = int(sys.stdin.readline().strip())
lst = []
amm = 0
for i in range (0, Q):
    inp = sys.stdin.readline().strip().split()
    num = int(inp[1])
    if inp[0] == 'A':
        amm += 1
        sum += num
        lst.append(num)
    else:
        amm -= 1
        sum -= num
        lst.remove(num)
    if amm > 0: print(min(lst), max(lst), round(sum/len(lst), 6))
    else: print('-1 -1 -1')
