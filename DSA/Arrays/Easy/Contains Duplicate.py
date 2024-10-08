'''
217. Contains Duplicate         https://leetcode.com/problems/contains-duplicate/description/
Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
# Approach 1
# Using Dictionaries.
from collections import Counter
def containsDuplicate(nums):
    freq=Counter(nums)
    for key,val in freq.items():
        if val>=2:
            return True
    
    return False

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))

# Approach 2
# Using Sets
def containsDuplicate1(nums):
    ans=set()
    for i in nums:
        if i in ans:
            return True
        else:
            ans.add(i)
    
    return False

print(containsDuplicate1(nums))