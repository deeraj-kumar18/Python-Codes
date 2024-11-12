'''
1832. Check if the Sentence Is Pangram          https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
Easy

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false
 
Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
'''
# Approach 1 using For Loop
'''
TC: O(N)
SC: O(1)
'''
def checkIfPangram(sentence):
    """
    :type sentence: str
    :rtype: bool
    """
    if len(sentence)<26:
        return False

    alpha="qwertyuiopasdfghjklzxcvbnm"
    c=0
    for i in alpha:
        if i in sentence:
            c+=1
    
    if c==26:
        return True
    else:
        return False

testcases=["thequickbrownfoxjumpsoverthelazydog","leetcode","jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"]
for testcase in testcases:
    print(checkIfPangram(testcase))