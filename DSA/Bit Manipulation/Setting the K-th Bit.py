"""
Setting the K-th Bit
Given a number and a value k, set the kth index in the number.
"""
def setBit(n,k):
    # We left shift 1 k times to get it to the kth index, and we perform OR operation with our number.
    return 1<<k | n

print(setBit(13,1))  