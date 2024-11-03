'''
20. Valid Parentheses

Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
# Approach using Stack
'''
1) We store the closing brackets as keys and opening brackets as values in a dictionary.
2) Iterate over the string and if the character is not a closing bracket, we append it to our stack.
3) If it is a closing bracket and if the stack is not empty, we pop the top most element and check if it is the same as value for that character in dictionary. 
4)If they are not equal we return false.
5) At the end, if the stack is empty, we return true else False.
'''
def isValid(s):
    ans=[]
    dict={")":"(" , "}":"{" , "]":"["}

    for char in s:
        if char in dict and ans:
            if dict[char]!=ans.pop():
                return False
        else:
            ans.append(char)
    
    return True if not ans else False 

testcases=["()","()[]{}","(]","([])","[","(){}}{"]
for testcase in testcases:
    print(isValid(testcase))