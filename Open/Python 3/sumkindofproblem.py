import sys
P = int(sys.stdin.readline())
for _ in range(P):
    K, N = map(int, sys.stdin.readline().strip().split())
    print(K, (N*N+N)//2, N*N, N*N+N)
