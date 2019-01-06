n = int(input())

if(n<1):
    ans = int(1-(n-1)*n//2)
else:
    ans = int(int(n+1)*n//2)
print(ans)
