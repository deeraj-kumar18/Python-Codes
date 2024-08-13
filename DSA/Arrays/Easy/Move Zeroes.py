'''
283. Move Zeroes   https://leetcode.com/problems/move-zeroes/description/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 
Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''

# APPROACH
'''
Using Two pointers. One pointer points at zero and other pointer iterates over the list to find non zero element 
and swaps it with first pointer.
'''

def move_zeroes(nums):
    return