'''
367. Valid Perfect Square  https://leetcode.com/problems/valid-perfect-square/description/

Easy

Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

Constraints:
1 <= num <= 2**31 - 1
'''
# Naive Approach
# TC: O(√n)
def isPerfectSquare(num):
    for i in range(1,int(num**0.5)+1):
        if i*i==num:
            return True
    
    return False

print(isPerfectSquare(25))

# Binary Search Approach
def isPerfectSquare1(num):
    if num<1:
        return False
    
    left,right=1,num

    while left<=right:
        mid=(left+right)//2
        sqaure=mid*mid
        if sqaure==num:
            return True
        elif sqaure<num:
            left=mid+1
        else:
            right=mid-1
    
    return False

print(isPerfectSquare1(295))