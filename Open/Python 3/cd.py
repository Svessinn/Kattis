def main():
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
          break
        jack = set()
        common = 0
        for i in range(N+M):
          cd = input()
          if i < N:
              jack.add(cd)
          else:
              if cd in jack:
                common += 1
        print(common)
main()
