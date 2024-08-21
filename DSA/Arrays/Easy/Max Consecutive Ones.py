'''
485. Max Consecutive Ones https://leetcode.com/problems/max-consecutive-ones/
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
 
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
# ACCESSING EACH ELEMENT IN THE LIST AS A MEMBER
def findMaxConsecutiveOnes(nums):
    max_ones=0
    count=0
    for i in nums:
        if i == 1:
            count+=1
            if count>=max_ones:
                max_ones=count
        else:
            count=0

    return max_ones

nums = [1,1,1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))

# ACCESSING EACH ELEMENT BY INDEX
def findMaxConsecutiveOnes1(nums):
    max_ones = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count +=1 
            if max_ones <= count:
                max_ones = count
        else:
            count = 0
    return max_ones

nums = [1,1,1,1,0,1,1,1]
print(findMaxConsecutiveOnes1(nums))