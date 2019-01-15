def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
inp = int(input())
while True:
    if (inp/sum_digits(inp) != inp//sum_digits(inp)):
        inp += 1
    else:
        print(inp)
        break
