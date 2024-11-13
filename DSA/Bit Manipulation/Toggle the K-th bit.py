"""
Given a number and an index k, toggle the bit at that index.
0 -> 1
1 -> 0
"""
def toggleBit(n,k):
    return n ^ (1<<k)

print(toggleBit(13,1))