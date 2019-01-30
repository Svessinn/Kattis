import math, sys
K = int(sys.stdin.readline())
num = str(oct(K))[1::]
num1 = num
try:
    for i in range(len(num)-1, -1, -1):
        if num[i] == '0':
            num = str(int(int(num) -math.pow(10, (len(num) - i - 1))))
        elif num[i] == '9' and num1[i] == '0':
            num = str(int(int(num) - math.pow(10, (len(num) - i - 1)) * 2))
    print(num[1::])
except ValueError:
    print('Error')
