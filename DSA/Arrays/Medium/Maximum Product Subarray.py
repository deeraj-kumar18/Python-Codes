'''
152. Maximum Product Subarray      https://leetcode.com/problems/maximum-product-subarray/description/
Medium
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
'''
# BruteForce Approach 
''' Create all subarrays and find the maximum product. 
TC: O(N^3)
SC: O(1)
'''
def maxProduct(nums):
    max_prod=float('-inf')
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            prod=1
            for k in range(i,j+1):
                prod*=nums[k]
            max_prod=max(prod,max_prod)
        
    return max_prod

testcases=[[2,3,-2,4],[-2,0,-1]]
for testcase in testcases:
    print(maxProduct(testcase))
    
# Does not work for large testcases.