from datetime import date
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day, month = map(int, input().split())
date = date(2009, month, day)
print(days[date.weekday()])
