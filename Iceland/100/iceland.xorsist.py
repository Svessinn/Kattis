inp = int(input())
func = lambda x: (x, 1, x+1, 0)[x%4]
result = func(inp)
print(result if 1 <= result <= inp else 'Enginn' if result == 0 else 'Gunnar')
