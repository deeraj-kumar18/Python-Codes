'''
Second Largest
Given an array arr, return the second largest distinct element from an array.
 If the second largest element doesn't exist then return -1.
'''
# BRUTE FORCE APPROACH Time Complexity : O(NlogN)
def second_largest_bruteforce(arr):
    a=list(set(arr))
    a.sort()
    return a[-2]

#  BETTER APPROACH  Time Complexity : O(2N)
def second_largest_better(arr): 
    largest=arr[0]
    for i in range(len(arr)):
        if(arr[i]>=largest):
            largest=arr[i]

    second_largest=float('-inf')  # If there are Negative numbers.
    for i in range(len(arr)):
        if(arr[i]>second_largest and arr[i]!=largest):
            second_largest=arr[i]

    return second_largest

# OPTIMAL APPROACH Time Complexity : 
def second_largest_optimal(arr):
    largest=arr[0]
    second_largest=float('-inf')
    for i in range(1,len(arr)):
        if(arr[i]>largest):
            second_largest=largest
            largest=arr[i]
        elif(arr[i]<largest and arr[i]>second_largest):
            second_largest=arr[i]

    return second_largest

arr=[1,7,8,6,4,2]
print(second_largest_bruteforce(arr))
print(second_largest_better(arr))
print(second_largest_optimal(arr))
