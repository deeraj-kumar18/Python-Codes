'''
136. Single Number

Easy

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
 
Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''
# Approach using Bit Manipulation
'''
when we XOR same values, we get a 0 and the number occuring once will remain.
'''
def singleNumber(nums):
    ans=0
    for num in nums:
        ans=ans^num
    
    return ans

nums = [4,1,2,1,2]
print(singleNumber(nums))