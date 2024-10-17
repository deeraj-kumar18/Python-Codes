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

i=1
# Test case 1: s is a subsequence of t
s1 = "abc"
t1 = "ahbgdc"
# Expected output: True
print(f"TestCase {i}",isSubsequence(s1, t1))
i+=1
# Test case 2: s is not a subsequence of t
s2 = "axc"
t2 = "ahbgdc"
# Expected output: False
print(f"TestCase {i}",isSubsequence(s2, t2))
i+=1
# Test case 3: s is an empty string
s3 = ""
t3 = "ahbgdc"
# Expected output: True (empty string is a subsequence of any string)
print(f"TestCase {i}",isSubsequence(s3, t3))
i+=1
# Test case 4: t is an empty string, s is non-empty
s4 = "abc"
t4 = ""
# Expected output: False (non-empty s cannot be a subsequence of an empty string)
print(f"TestCase {i}",isSubsequence(s4, t4))
i+=1

# Test case 5: s and t are the same
s5 = "abc"
t5 = "abc"
# Expected output: True (s is exactly t, so it's a subsequence)
print(f"TestCase {i}",isSubsequence(s5, t5))
i+=1
