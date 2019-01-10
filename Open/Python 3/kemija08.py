import sys
vowels = 'aeiou'
inp = sys.stdin.readline()

skip = 0
for char in inp:
    if skip > 0:
        skip -= 1
        
    else:
        print(char, end="")
        for vowel in vowels:
            if char == vowel:
                skip = 2
