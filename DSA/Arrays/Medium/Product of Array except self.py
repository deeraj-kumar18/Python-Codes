'''
238. Product of Array Except Self
Medium
Topics

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''
# BruteForce Approach 
'''
Approach: Iterating the list using two for loops and calculating the product.
TC: O(N^2)
SC: O(N)
'''
def productExceptSelf(nums):
    ans=[]
    for i in range(len(nums)):
        prod=1
        for j in range(len(nums)):
            if i==j:
                continue
            else:
                prod*=nums[j]
        ans.append(prod)
    
    return ans

testcases=[[1,2,3,4],[-1,1,0,-3,3]]
for testcase in testcases:
    print(productExceptSelf(testcase))

# Does not work for large testcases as we are iterating twice. 

# Optimal Approach 