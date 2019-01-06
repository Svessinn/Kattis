K = int(input())
num = 0
counter = 1
while counter < K:
    if '0' in str(num) or '8' in str(num):
        num += 1
    else:
        counter += 1
        num += 1
if '0' in str(num) or '8' in str(num):
    num += 1
print(num)
