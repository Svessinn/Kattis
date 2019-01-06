Total = 0
Winner = 0

for i in range(1,6):
    a, b, c, d = map(int,input().split())
    Tot = a + b + c + d
    if Tot > Total:
        Winner = i
        Total = Tot
print(Winner, Total)
