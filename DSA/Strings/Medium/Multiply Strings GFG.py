'''
Multiply two strings        https://www.geeksforgeeks.org/problems/multiply-two-strings/1?page=2&sortBy=submissions

Difficulty: Medium

Given two numbers as strings s1 and s2. Calculate their Product.

Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. There can be zeros in the begining of the numbers. You don't need to specify '+' sign in the begining of positive numbers.

Example 1:
Input:
s1 = "0033"
s2 = "2"
Output:
66

Example 2:
Input:
s1 = "11"
s2 = "23"
Output:
253

Expected Time Complexity: O(n1* n2)
Expected Auxiliary Space: O(n1 + n2); where n1 and n2 are sizes of strings s1 and s2 respectively.

Constraints:
1 ≤ length of s1 and s2 ≤ 103
'''
# Own Approach
def multiplyStrings(s1,s2):
    # return the product string
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
        
    return no1*no2

s1 = "0033"
s2 = "2"
print(multiplyStrings(s1,s2))