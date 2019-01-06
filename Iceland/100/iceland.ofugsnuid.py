numlist = []
num = int(input())

for i in range(num):
    num_to_add = int(input())
    numlist.append(num_to_add)

numlistbackwards = (numlist[::-1])
for i in numlistbackwards:
    print(i)
