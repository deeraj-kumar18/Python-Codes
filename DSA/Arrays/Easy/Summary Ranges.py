"""
228. Summary Ranges     https://leetcode.com/problems/summary-ranges/description/
Easy

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 
Constraints:
0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""
def summaryRanges(nums):
    if not nums: # if it is an empty list, return empty list.
        return []
    
    ans=[]
    start=nums[0]  # we start the range here.

    for i in range(1,len( nums)):
        if nums[i]!=nums[i-1]+1: # if the current number is NOT greater than the previous number by 1
            if start!=nums[i-1]: # if the start and last consecutive number are not same, then its range of numbers.
                ans.append("{} --> {}".format(start,nums[i-1]))
            else: # we append the single number if the start and nums[i-1] are at same position.
                ans.append(str(nums[i-1]))
            start=nums[i] # updating the start to the current number.

      # Handle the last range
    if start!=nums[-1]:
        ans.append("{} --> {}".format(start,nums[-1]))
    else:
        ans.append(str(start))

    return ans

nums=[0,1,2,4,5,7]
print(summaryRanges(nums))