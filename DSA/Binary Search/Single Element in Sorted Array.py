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
# Naive Approach using A For loop
'''
TC:O(n)
'''
def singleNonDuplicate0(nums):
    n=len(nums)
    # Edge case, only one element.
    if n==1:
        return nums[0]
    
    for i in range(n):
        # First element only has element on its Right.
        if i==0:
            if nums[i]!=nums[i+1]:
                return nums[i]
        # Last element only has element on its Left.
        elif i==n-1:
            if nums[i]!=nums[i-1]:
                return nums[i]
        # For all the middle elements, we check the left and right elements and both of them
        #  are not equal. then it is Single Element.
        else:
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]

nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate0(nums))

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