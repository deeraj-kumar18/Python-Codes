'''
231. Power of Two

Easy

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false
 
Constraints:
-2**31 <= n <= 2**31 - 1

Follow up: Could you solve it without loops/recursion?
'''
# Brute Force Approach
def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n==1:
        return True
    x=1
    for i in range(1,32):
        x*=2
        if x==n:
            return True
        if x>n:
            return False
    
    return False

print(isPowerOfTwo(128))

# O(1) Solution, Optimal Solution
def isPower(n):
    if n==0:
        return False
    if n &(n-1)==0:
        return True
    else:
        return False

print(isPowerOfTwo(128))

