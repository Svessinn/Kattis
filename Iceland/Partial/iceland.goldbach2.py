lower = 2
upper = int(input())
primes = []
primes1 = []
primes2 = []

for num in range(lower,upper):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           primes.append(num)
           
x = upper - primes[len(primes)-2]
x1 = primes[len(primes)-2]

for num in range(lower,x):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           primes1.append(num)
           
y = x - primes1[len(primes1)-2]
y1 = primes1[len(primes1)-2]
print(x1, y1, y)
