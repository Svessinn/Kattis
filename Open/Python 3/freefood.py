N = int(input())
st = set()
for i in range(N):
    s, t = map(int, input().split())
    for i in range(s, t+1):
        st.add(i)
print(len(st))
