'''
704. Binary Search
Easy
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''
def binary_search(nums, target):
    n=len(nums)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        # print(mid)
        if nums[mid]==target:
            return mid
        elif target>nums[mid]: # If the target element is greater than mid element, we search the RIGHT half
            low=mid+1       
        else:
            high=mid-1  # If the target element is lesser than mid element, we search the LEFT half

    return -1   

nums = [-1,0,3,5,9,12]
target = 69
print(binary_search(nums,target))