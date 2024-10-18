'''
344. Reverse String         https://leetcode.com/problems/reverse-string/description/

Easy

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 
Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
'''
# TC: O(n/2)
# SC: O(1)
def reverseString(s):
    n=len(s)
    for i in range(n//2):
        s[i],s[n-i-1]=s[n-i-1],s[i]
        
    return s

s = ["h","e","l","l","o"]
print(reverseString(s))

# Approach using inbuilt Reverse function
def reverseString1(s):
    s.reverse()
    return s
s1 = ["h","e","l","l","o"]
print(reverseString1(s1))