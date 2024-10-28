'''
3136. Valid Word

Easy

A word is considered valid if:
It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
 
Example 1:
Input: word = "234Adas"
Output: true
Explanation:
This word satisfies the conditions.

Example 2:
Input: word = "b3"
Output: false
Explanation:
The length of this word is fewer than 3, and does not have a vowel.

Example 3:
Input: word = "a3$e"
Output: false
Explanation:
This word contains a '$' character and does not have a consonant.

Constraints:
1 <= word.length <= 20
word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.
'''
def isValid(word):
    """
    :type word: str
    :rtype: bool
    """
    if len(word)<3:
        return False
    word=word.lower()
    alnum="1234567890qwertyuiopasdfghjklzxcvbnm"
    vowels='aeiou'
    consonants='qwrtypsdfghjklzxcvbnm'
    v_c,cons_c=0,0
    for i in word:
        if i not in alnum:
            return False
        if i in vowels:
            v_c+=1
        if i in consonants:
            cons_c+=1
    
    if v_c<1 or cons_c<1:
        return False
    
    return True

word = "234Adas"
print(isValid(word))

# Leetcode Approach
def isValid1(word):
    """
    :type word: str
    :rtype: bool
    """
        
    for letter in word:
        if not letter.isalnum():
            return False

    if len(list(word)) < 3:
        return False

    numOfVowels = 0
    numOfConsonants = 0

    for letter in word:
        if letter.lower() in ["a","e","i","o","u"]:
            numOfVowels += 1
        else:
            if letter.isalpha():
                numOfConsonants += 1

    if numOfVowels == 0 or numOfConsonants == 0:
        return False
    return True