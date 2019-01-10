G, S, C = map(int, input().split())
gold = 6
silver = 3
copper = 0
prov = 8
duchy = 5
estate = 2
tot = (G*3)+(S*2)+C
if tot < 2: print('Copper')
elif tot < 3: print('Estate or Copper')
elif tot < 5: print('Estate or Silver')
elif tot < 6: print('Duchy or Silver')
elif tot < 8: print('Duchy or Gold')
else: print('Province or Gold')
