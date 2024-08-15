'''
Second Smallest
Given an array arr, return the second smallest distinct element from an array.
 If the second smallest element doesn't exist then return -1.
'''
# BRUTEFORCE APPROACH
def second_smallest_bruteforce(arr):
    a=list(set(arr))
    a.sort()
    if len(a)==1:
        return a[0]
    return a[1]

arr=[12, 35, 1, 10, 34, 1] 
arr1=[1,10,12,8]*10 
arr2=[12, 35, 1, 7,8, 34, 1]
print(second_smallest_bruteforce(arr),second_smallest_bruteforce(arr1),second_smallest_bruteforce(arr2))