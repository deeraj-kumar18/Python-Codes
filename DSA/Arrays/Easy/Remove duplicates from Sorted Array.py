'''
26. Remove Duplicates from Sorted Array   https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5.
'''
def remove_duplicates(arr):
    slow=0
    fast=1
    while fast<len(arr):
        if arr[slow]==arr[fast]:
            fast+=1
        else:
            arr[slow+1]=arr[fast]
            fast+=1
            slow+=1
    
    return slow+1

# Initial Testing
# arr=[0,0,1,1,1,2,2,3,3,4]

# TESTCASES
test_cases = [
    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],  # Expected Output: 5, array after function call: [0, 1, 2, 3, 4, _, _, _, _, _]
    [1, 1, 2],  # Expected Output: 2, array after function call: [1, 2, _]
    [1, 1, 1, 1],  # Expected Output: 1, array after function call: [1, _, _, _]
    [1, 2, 3, 4, 5],  # Expected Output: 5, array after function call: [1, 2, 3, 4, 5]
    [0, 0, 0, 0, 0],  # Expected Output: 1, array after function call: [0, _, _, _, _]
    [1, 1, 2, 3, 3, 4, 4, 5, 5],  # Expected Output: 5, array after function call: [1, 2, 3, 4, 5, _, _, _, _]
    [2, 2, 2, 2, 2, 2],  # Expected Output: 1, array after function call: [2, _, _, _, _, _]
    [],  # Expected Output: 0, array after function call: []
    [3, 3, 3, 3],  # Expected Output: 1, array after function call: [3, _, _, _]
    [1, 2, 2, 2, 3],  # Expected Output: 3, array after function call: [1, 2, 3, _, _]
]

for testcase in test_cases:
    print(remove_duplicates(testcase))
