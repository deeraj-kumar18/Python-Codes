'''
1768. Merge Strings Alternately     https://leetcode.com/problems/merge-strings-alternately/description/
Easy

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 
Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
'''
# Approach 1 Using Two Pointers
'''
TC: O(N)
'''
def mergeAlternately(word1, word2):
    i,j=0,0
    ans=""
    flag=1
    while i<len(word1) and j<len(word2):
        if flag:
            ans+=word1[i]
            i+=1
            flag=0
        else:
            ans+=word2[j]
            j+=1
            flag=1
    
    while i<len(word1):
        ans+=word1[i]
        i+=1

    while j<len(word2):
        ans+=word2[j]
        j+=1
    
    return ans

print(mergeAlternately("aue","nde"))
print(mergeAlternately("abcd","pq"))

# Approach 2
def merge(word1,word2):
    len1,len2=len(word1),len(word2)
    ans=""
    for i in range(min(len1,len2)):
        ans+=word1[i]
        ans+=word2[i]
    
    if len1>len2:
        ans+=word1[len2:] 
    else:
        ans+=word2[len1:]

    return ans


print(merge("aue","nde"))
print(merge("abcd","pq"))