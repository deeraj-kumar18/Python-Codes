'''
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''
# BRUTE FORCE SOLUTION
# Iterate the list using two loops and return the indices if the calculated sum of two elements 
# is equal to target.
def twosum(nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]

# Initial Testing
# nums = [2,7,11,15]
# nums = [1,3,34,7,11,23]
# target = 9
# target = 18
# result=twosum(nums,target)
# print(result)

# Testing with testcases
testcases=[([2,7,11,15],9),([1,3,34,7,11,23],18),([3,2,4],6),([3,3],6)]
print("Brute Force Solution")
for testcase in testcases:
    print(twosum(testcase[0],testcase[1]))


# OPTIMAL SOLUTION
# we iterate through the list and 
# we find the difference between the target and current number
# We are storing the number and its index in a dictionary,
#  if we find the diff in dict, we found the complimenting value of current number to get the
#  sum as target number. hence we return the indices.
#  else we add the current number as key and its index as value into the dictionary. 
def twosum1(nums,target):
    dict={}
    for i,num in enumerate(nums):
        diff = target - num
        if diff in dict:
            # print(dict)
            return [dict[diff],i]

        dict[num]=i
    
# Initial Testing
# nums = [2,7,11,15]
# nums = [1,3,34,7,11,23]
# target = 9
# target = 18   
# result=twosum(nums,target)
# print(result)

# Testing with testcases
testcases=[([2,7,11,15],9),([1,3,34,7,11,23],18),([3,2,4],6),([3,3],6)]
print("Optimal Solution")
for testcase in testcases:
    print(twosum1(testcase[0],testcase[1]))