'''
392. Is Subsequence     https://leetcode.com/problems/is-subsequence/description/
Easy

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
 
Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
'''

def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # Edge Cases
    if (len(s) > len(t) or (len(t) == 0 and len(s)!= 0)):
        return False
    if (len(s) == 0):
        return True
    # Two-pointer approach
    i, j = 0, 0  # i is for s, j is for t

    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            i+=1 # Move i only if characters match
        j+=1 # Always move j to continue scanning t
    
    # If i has moved through the entire string s, then s is a subsequence of t
    return i == len(s)

s = "abc"
t = "ahbgdc"

print(isSubsequence(s,t))