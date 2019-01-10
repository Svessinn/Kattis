s = str(input())
days = 0
per = ['P', 'E', 'R']
for i in range(0, len(s)):
    if s[i] != per[i%3]:
        s.replace(s[i], per[i%3])
        days += 1
print(days)
