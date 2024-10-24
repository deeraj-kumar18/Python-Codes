"""
1002. Find Common Characters            https://leetcode.com/problems/find-common-characters/description/

Easy

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""
def find_common(words):
    ans=list(words[0])
    for word in words[1:]:
        op=[]
        for char in ans:
            if char in word:
                op.append(char)
                word=word.replace(char,"",1)
        
        ans=op
    
    return ans

words = [["bella","label","roller"],["cool","lock","cook"]]
for testcase in words:
    print(find_common(testcase))