'''
242. Valid Anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''
from collections import Counter
def isAnagram(s, t):
    d1=Counter(s)
    d2=Counter(t)

    return d1==d2

s = "anagram"
t = "nagaraam"
print(isAnagram(s,t))