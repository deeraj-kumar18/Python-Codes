'''
81. Search in Rotated Sorted Array II       https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
Medium

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 
Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
'''
# Approach
'''
The major issue arises when the duplicates are in low, mid and high positions at the same time. At this
condition our previous code breaks. Hence we need to resolve the condition 
arr[low] == arr[mid] == arr[high]
WE shrink our search space by one element each on left and right side. 
TC: O(log n) for average case
TC: O(n/2) for worst case
'''
def search_binary(nums,target):
    low,high=0,len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        
        # Condition
        if nums[low]==nums[mid]==nums[high]:
            low+=1
            high-=1
            continue
        # Finding for Sorted Half.
        # Left Half Sorted Array 
        if nums[low]<=nums[mid]:
            # Eliminatimg the search space by comparing values of low, mid and high
            if nums[low]<=target and target<=nums[mid]:
                high=mid-1
            else:
                low=mid+1
        
        # Right Half Sorted Array
        if nums[mid]<=nums[high]:
            if nums[mid]<=target and target<=nums[high]:
                low=mid+1
            else:
                high=mid-1

    return False

nums = [2,5,6,0,0,1,2]
target = 3
print(search_binary(nums,target))