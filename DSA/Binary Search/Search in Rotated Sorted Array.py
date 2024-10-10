'''
33. Search in Rotated Sorted Array
Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
 
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''
# BruteForce Approach Using Built-in methods
'''
Using the "in" operator and .index() method to find the necessary index.
TC: O(N)
SC: O(1)
'''
def search(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        return -1

nums =[4,5,6,7,0,1,2]
target=0
print(search(nums,target))

# Conventional BruteForce Approach
'''
Run a loop to check if the target element is found in the list and return its index.
TC: O(N)
SC: O(1)
'''
def search1(nums, target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i 

    return -1

print(search1(nums,target))

# Optimal Approach
'''
As we see the keywords sorted and search, Binary Search strikes our mind. Here we need to modify our 
binary search as we are working on an Rotated Sorted Array, we cannot go forward with our conventional
Binary search algo. 
1. We find which part of the array is sorted.
2. Eliminate the search space by comparing values of low, mid and high.

TC: O(log n)
SC: O(1)
'''
def search_binary(nums,target):
    return