"""
Setting the K-th Bit
Given a number and a value k, set the kth index in the number.
"""
def setBit(n,k):
    return 1<<k | n

print(setBit(13,1))  