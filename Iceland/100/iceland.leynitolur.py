import sys

for i in sys.stdin.read().strip().split():

    y = (int(i) - 68431307) * 881051043651 % (2**64)
    assert 0 <= y <= 10**18
    assert (y*230309227 + 68431307) % (2**64) == int(i)

    print(y)
