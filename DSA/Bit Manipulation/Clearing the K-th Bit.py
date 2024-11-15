"""
Clearing the K-th Bit
Given a number and a value k, clear the kth index in the number.
"""
def clearBit(n,k):
    # First , we create a power of 2 number with value k by left shifting 1 . 
    num=1<<k
    
    # Then we negate the number. so that except the kth index, we have all 1's except the kth index.
    num=~num 
    # We perform bitwise AND operation, which will result in clearing of kth bit.
    return num & n

print(clearBit(13,2)) 