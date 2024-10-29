'''
242. Valid Anagram      https://leetcode.com/problems/valid-anagram/description/
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
# Dictionary approach
from collections import Counter
def isAnagram(s, t):
    # Creating dictionaries with frequencies of characters in the string.
    d1=Counter(s)
    d2=Counter(t)

    # If the frequencies of characters are same in the two dictionaries, we return True else False.
    return d1==d2

s = "anagram"
t = "nagaraam"
print(isAnagram(s,t))

# Using Sets
def isAnagram1(s,t):
    if len(s)!=len(t):
        return False

    unique_letters=set(s)

    for letter in unique_letters:
        if s.count(letter)!=unique_letters.count(letter):
            return False
    
    return True 

s = "anagram"
t = "nagaraam"
print(isAnagram(s,t))