'''
53. Maximum Subarray    https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 '''
# BruteForce Approach
'''
Use 2 for loops and calculate the sum and compare it with maximum sum. 
Time Complexity: O(n^2)
Space Complexity: O(1)
'''
def max_subarray_sum(nums):
    max_sum=float('-inf')
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            sum1=sum(nums[i:j])
            if sum1>=max_sum:
                max_sum=sum1
    return max_sum

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(nums))

# Optimal Approach
'''
Kadane's Algorithm
Our goal is to iterate over the list only once to achieve time complexity of O(N)
We iterate over the array adding each element to our sum variable and check if the sum is greater 
than max_sum, if yes, we update the max_sum. If sum is less than 0, then we update the sum to 0.
after iterating throughout the list, we will have the maximum sum in our variable, we will return that. 
TC: O(N)
SC: O(1)
'''
def max_subarray_sum_opt(nums):
    max_sum=0
    summ=0
    for i in range(len(nums)):
        summ+=nums[i]
        if summ > max_sum:
            max_sum=summ
        if summ<0:
            summ=0
    
    return max_sum

print(max_subarray_sum_opt(nums))