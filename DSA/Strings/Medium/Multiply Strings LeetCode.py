'''
43. Multiply Strings        https://leetcode.com/problems/multiply-strings/description/

Medium

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
 
Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''
# Own Approach
'''
1)Stored each digit as a string as key and integer value as value in a dictionary.
2)Iterating every string from the end and formulating the number using the dictionary.
3)Checking for negative numbers.'''
def multiply(s1, s2):
    dic={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    no1=0
    j=1
    for i in range(len(s1)-1,-1,-1):
        if s1[i] in dic:
            no1+=dic[s1[i]]*j
            j*=10
            
    if s1[0]=="-":
        no1*=-1
        
    no2=0
    j=1
    for i in range(len(s2)-1,-1,-1):
        if s2[i] in dic:
            no2+=dic[s2[i]]*j
            j*=10
    
    if s2[0]=="-":
        no2*=-1
        
    return str(no1*no2)

