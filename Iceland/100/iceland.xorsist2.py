inp = int(input())
a, b = map(int, input().split())
func = lambda x: (x, 1, x+1, 0)[x%4]
result = func(a-1)^func(b)
print(result if 1 <= result <= inp else 'Enginn' if result == 0 else 'Gunnar')
