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
''' 
Create all subarrays and find the maximum product. 
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

# Better Approach
'''
Create all subarrays and find the maximum product in the second loop itself. 
TC: O(N^2)
SC: O(1)
'''
def maxProduct1(nums):
    max_prod=float('-inf')
    for i in range(len(nums)):
        prod=1
        for j in range(i,len(nums)):
            prod*=nums[j]
            max_prod=max(prod,max_prod)
        
    return max_prod

for testcase in testcases:
    print(maxProduct1(testcase))
# Does not work for all large testcases.

# Optimal Solution
'''
We try to solve it in O(N) TC.
Approach:
We calculate prefix(from front) and suffix (from back) product for each element and return the maximum product we 
encounter while traversing the array.
TC: O(N)
SC: O(1)
'''
def maxProduct2(nums):
    n=len(nums)
    pref=1
    suff=1
    maxi=float('-inf')
    for i in range(n):
        if pref==0:  # Case when we encounter a Zero in the array, then the product will become zero, so we make it back to 1
            pref=1
        if suff==0:
            suff=1 
        
        pref*=nums[i]
        suff*=nums[n-i-1]
        maxi=max(maxi,max(pref,suff))
    
    return maxi

for testcase in testcases:
    print(maxProduct2(testcase))