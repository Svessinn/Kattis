def dec_to_bin(x):
    return bin(x)[2:]
def reverse(x):
    return x[::-1]
def bin_to_dec(x):
    return int(x, 2)
print(bin_to_dec(reverse(dec_to_bin(int(input())))))
