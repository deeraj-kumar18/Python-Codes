'''
451. Sort Characters By Frequency       https://leetcode.com/problems/sort-characters-by-frequency/description/

Medium

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Constraints:
1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
'''
# Own Approach
from collections import Counter
def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    # Frequency count of characters in the String.
    a=Counter(s)

    # List of Sorted Dictionary using frequency in Descending Order.  
    sorted_a=sorted(a.items(),key = lambda value:value[1],reverse=True)
    # print(sorted_a)        
    ans=""
    # Iterating over the list
    for k,v in sorted_a:
        # Concatenating each character for number the number of times it occurs.
        ans+=k*v
    
    return ans


s = "ccaaa"
print(frequencySort(s))
        
# Using get keyword in Dictionary.
def frequencySort1(s):
    # Dictionary
    freq=dict()
    # Incrementing the count by 1 
    for c in s:
        freq[c] = freq.get(c,0) + 1
    
    items=freq.items()
    sort_arr=sorted(items,key=lambda x:x[1],reverse=True)

    res_str=""
    for c,f in freq.items():
        res_str+=c*f
    
    return res_str

s = "ccccaaa"
print(frequencySort1(s))