'''
14. Longest Common Prefix       https://leetcode.com/problems/longest-common-prefix/description/ 
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

# TC: O(N)
# SC: O(1)
def longestCommonPrefix(strs):
    # Edge Case: When the input is an empty string.
    if strs == "":
        return ""
    
    # To make sure we dont go out of bounds, we iterate over the smallest string in the input list.
    min_len=min(len(string) for string in strs)

    for i in range(min_len):
        # Check the character at position i in all strings
        current_char=strs[0][i]
        for string in strs:
            if current_char!=string[i]:
                return strs[0][:i]
    
    return strs[0][:min_len]         # All characters matched, return full prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))