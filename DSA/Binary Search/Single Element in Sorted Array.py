'''
540. Single Element in a Sorted Array       https://leetcode.com/problems/single-element-in-a-sorted-array/description/
Medium

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 105
'''
# Approach using Dictionary
'''
TC: O(n)
SC: O(n)
'''
from collections import Counter
def singleNonDuplicate(nums):
    dict=Counter(nums)
    for key,val in dict.items():
        if val==1:
            return key

nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))