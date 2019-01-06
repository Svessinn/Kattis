N = int(input())
a, b = map(int, input().split())
total = 0
for i in range(a, b+1):
    total = total ^ i
if total > N:
    print('Gunnar')
elif total == 0:
    print('Enginn')
else:
    print(total)
