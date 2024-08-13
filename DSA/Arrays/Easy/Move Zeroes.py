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
    last_non_zero=0
    j=0

    while(j<len(nums)):
        if nums[j]!=0:
            nums[last_non_zero],nums[j]=nums[j],nums[last_non_zero]
            last_non_zero+=1
        j+=1

    return nums

# Inital Testing
# arr=[0,1,0,3,12]
# print(move_zeroes(arr))

# TESTCASES
testcases=[[0,1,0,3,12],[0,0,1,2,0,3,4],[0,0,1,2,0,3,4],[4,0,0,2,0,1],[4],[0, 0, 0, 0, 5],
           [1, 2, 3, 4, 0, 0, 0],[1, 0, 2, 0, 3, 0, 4],[0, 0, 0]]

for testcase in testcases:
    print(move_zeroes(testcase))

