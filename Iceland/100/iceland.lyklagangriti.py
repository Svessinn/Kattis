import sys
n = sys.stdin.readline().strip()
idx = 0
word = []
for letter in n:
  if letter == "L" and idx >= 1:
    idx -= 1
  elif letter == "B" and idx >= 1:
    idx -= 1
    word.pop(idx)
  elif letter == "R" and idx != len(word):
    idx += 1
  else:
    word.insert(idx,letter)
    idx += 1
  

print("".join(word))
