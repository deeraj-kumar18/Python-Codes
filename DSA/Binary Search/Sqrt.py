'''
69. Sqrt(x)     https://leetcode.com/problems/sqrtx/description/

Easy

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 
Constraints:
0 <= x <= 2**31 - 1
'''
# Brute Force Approach
def Sqrt(num):
    # Edge/Base cases
    if num==0 or num==1:
        return num
    
    result=1
    i=0
    # Till the result is less than or equal to the target number, we continue the loop.
    while result<=num:
        i+=1
        # Updating result value with square of each number till the breaking condition.
        result= i*i
    
    # Returning i-1 because the loop breaks after the squared value crosses the number, hence we return the before element.
    return i-1

print(Sqrt(80))            