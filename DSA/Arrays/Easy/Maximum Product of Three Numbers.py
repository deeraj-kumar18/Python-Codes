'''
628. Maximum Product of Three Numbers           https://leetcode.com/problems/maximum-product-of-three-numbers/

Easy

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6
 
Constraints:
3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
'''
def maximumProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    first=nums[0]*nums[1]*nums[-1]
    last=nums[-3]*nums[-2]*nums[-1]
    return max(first,last)

nums = [[1,2,3],[1,2,3,4],[-1,-2,-3]]
for testcase in nums:
    print(maximumProduct(testcase))