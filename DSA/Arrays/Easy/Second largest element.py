'''
Second Largest
Given an array arr, return the second largest distinct element from an array.
 If the second largest element doesn't exist then return -1.
'''
# BRUTE FORCE APPROACH
def second_largest(arr):
    a=list(set(arr))
    a.sort()
    return a[-2]

arr=[1,7,8,6,4,2]
print(second_largest(arr))
