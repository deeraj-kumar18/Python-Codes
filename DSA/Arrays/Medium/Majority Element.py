'''
169. Majority Element  https://leetcode.com/problems/majority-element/description/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''
# BruteForce Approach 
'''
iterate two loops and count the occurance each time, if occurance is 
greater than n//2, we return the number.
'''
def majority_brute(arr):
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
            
        if count>len(arr)//2:
            return arr[i]

nums =[2,2,1,1,1,1,1,2,2,3,3,3,3,3,3,3,3,3,3]
print(majority_brute(nums))