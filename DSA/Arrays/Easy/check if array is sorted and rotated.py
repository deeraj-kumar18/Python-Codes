'''
1752. Check if Array Is Sorted and Rotated

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

Example 1:
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
'''
def is_sorted_and_rotated(arr,n):
    count=0
    for i in range(n):
        if(arr[i]>arr[(i+1)%n]):
            count+=1
            if count>1:
                return False

    return True

# nums = [3,4,5,1,2]
# TESTCASES
test_cases = [
    [3, 4, 5, 1, 2],  # Expected Output: True
    [1, 2, 3, 4, 5],  # Expected Output: True
    [2, 1, 3, 4, 5],  # Expected Output: False
    [5, 1, 2, 3, 4],  # Expected Output: True
    [4, 5, 6, 1, 2, 3],  # Expected Output: True
    [1, 3, 2],  # Expected Output: False
    [10, 20, 30, 40, 50, 5],  # Expected Output: True
    [10, 20, 30, 40, 50],  # Expected Output: True
    [3, 2, 1, 5, 4],  # Expected Output: False
    [7, 9, 11, 12, 15],  # Expected Output: True
]
for testcase in test_cases:
    print(is_sorted_and_rotated(testcase,len(testcase)))