'''
205. Isomorphic Strings

Easy

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''
# Approach
'''
1)Initialise two dictionaries to store the mapping of each character from string1 to string2 and Vice versa
2)For each character,we keep the character of other string as a value for current character as key.
3)If the key already exists and the value is different, the condition BREAKS and we return False
4)After complete iteration, if we did not find any breaking condition, we Return TRUE'''
def isIsomorphic(s, t):
    # If the lengths of the strings are not equal, they cannot be isomorphic.
    if len(s)!=len(t):
        return 0
    
    StoTmap={}
    TtoSmap={}
    for i in range(len(s)):
        char1,char2=s[i],t[i]
        if((char1 in StoTmap and StoTmap[char1]!=char2) or (char2 in TtoSmap and TtoSmap[char2]!=char1)):
            return False
        
        StoTmap[char1]=char2
        TtoSmap[char2]=char1

    return True

s = "paper"
t = "title"
print(isIsomorphic(s,t))