import sys

Coke, n10, n50, n100 = [int(x) for x in sys.stdin.readline().strip().split()]

count = 0

while Coke > 0:
    if n100 > 0:
        if n100 + n50 >= Coke or n10 < 3:
            n100 -= 1
            n10 += 2
            count += 1
        else:
          n100 -= 1
          n10 -= 3
          n50 += 1
          count += 4
    elif n50 > 0:
        if n50 <= Coke:
            n50 -= 1
            n10 -= 3
            count += 4
        else:
          n50 -= 2
          n10 += 2
          count += 2
    else:
        n10 -= 8
        count += 8
    Coke -= 1
print(count)
