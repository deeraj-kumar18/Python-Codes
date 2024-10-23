'''
500. Keyboard Row      AUTOLAB  https://leetcode.com/problems/keyboard-row/description/
Easy

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
 
Constraints:
1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase). 
'''
# Own Approach 
def find_words(words):
    firstrow='qwertyuiopQWERTYUIOP'
    secondrow='asdfghjklASDFGHJKL'
    thirdrow='zxcvbnmZXCVBNM'
    output=[]

    for word in words:
        firstrowFlag=True
        secondrowFlag=True
        thirdrowFlag=True
        for char in word:
            if char not in firstrow:
                firstrowFlag=False
            if char not in secondrow:
                secondrowFlag=False
            if char not in thirdrow:
                thirdrowFlag=False
        
        if firstrowFlag:
            output.append(word)
        if secondrowFlag:
            output.append(word)
        if thirdrowFlag:
            output.append(word)
        
    return output

input=["Hello", "Alaska", "Dad", "Peace"]
print(find_words(input))
