def sumDigits(inp):
    return sum([int(x) for x in str(inp)])

L = int(input())
D = int(input())
X = int(input())

mn = 0
mx = 0

for i in range(L, D+1):
    if (sumDigits(i) == X):
        mn = i
        break

for i in range(D, L-1, -1):
    if (sumDigits(i) == X):
        mx = i
        break

print(mn)
print(mx)
