'''
34. Find First and Last Position of Element in Sorted Array  https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
Medium

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''
# BruteForce Approach 
'''
We iterate over the array and store the first and last occurance of the target element.
TC: O(N)
SC: O(1)
It takes long time for large testcases as we are iterating throughoout the list. We are not utilizing the 
Non decreasing arrangement property of the list. 
'''
def searchRange(nums,target):
    first,last=-1,-1 # default values if the element is not found.
    for i in range(len(nums)):
        if nums[i]==target:
            if first == -1:
                first=i   # First gets updated only on the first occurance.

            last=i  # Last gets updated on all occurances.
    
    return [first,last]

nums = [5,7,7,8,8,10]
target = 10
print(searchRange(nums,target))