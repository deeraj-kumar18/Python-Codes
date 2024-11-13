"""
Given a number and an index k, toggle the bit at that index.
0 -> 1
1 -> 0
"""
def toggleBit(n,k):
    # We left shift 1 by k times and perform XOR operation with number, the bit is toggled.
    return n ^ (1<<k)

print(toggleBit(13,1))