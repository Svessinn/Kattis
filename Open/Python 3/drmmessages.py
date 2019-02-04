def snua(inp):
    num = 0
    for i in inp:
        num += alphabet.find(i)
    snuinn = ''
    for i in inp:
        add = (num + alphabet.find(i)) % 26
        snuinn += alphabet[add]
    return snuinn

def sameina(w1, w2):
    sameinad = ''
    for i in range(len(w1)):
        add = (alphabet.find(w1[i]) + alphabet.find(w2[i])) % 26
        sameinad += alphabet[add]
    return sameinad

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
w = str(input())
split = len(w)//2
w1, w2 = w[:split], w[split:]
print(sameina(snua(w1), snua(w2)))
