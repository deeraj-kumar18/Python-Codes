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
'''
We create two arrays to calculate left product and right product of that element 
we multiply them back to get the answer.
TC:O(N)
SC:O(N)
'''
def productExceptSelf1(nums):
    l_mult=1
    r_mult=1
    n=len(nums)
    l_arr=[0]*n
    r_arr=[0]*n

    for i in range(n):
        j=-i-1
        l_arr[i]=l_mult
        r_arr[j]=r_mult
        l_mult*=nums[i]
        r_mult*=nums[j]

    ans=[0]*n
    for i in range(n):
        ans[i]=l_arr[i]*r_arr[i]

    return ans    


testcases=[[1,2,3,4],[-1,1,0,-3,3]]
for testcase in testcases:
    print(productExceptSelf1(testcase))

# similar approach 
def productExceptSelf2(self, nums):
    n = len(nums)
            
    left = [1] * n
    right = [1] * n
    result = [1] * n

    # Fill left array
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    # Fill right array
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    # Fill result array
    for i in range(n):
        result[i] = left[i] * right[i]

    return result