"""
Clearing the K-th Bit
Given a number and a value k, clear the kth index in the number.
"""
def clearBit(n,k):
    return ~(1<<k) & n

print(clearBit(13,2)) 