'''
2710. Remove Trailing Zeros From a String           https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/

Easy

Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

Example 1:
Input: num = "51230100"
Output: "512301"
Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

Example 2:
Input: num = "123"
Output: "123"
Explanation: Integer "123" has no trailing zeros, we return integer "123".
 
Constraints:
1 <= num.length <= 1000
num consists of only digits.
num doesn't have any leading zeros.

'''
# Naive Approach
def removeTrailingZeros(num):
    i=len(num)-1
    while i>=0:
        if num[i]=='0':
            i-=1
        else:
            return num[:i+1]
            break

    return num

# Using For loop

def removeTrailingZeros1(num):
    for i in range(len(num)-1,-1,-1):
        if num[i]!='0':
            return num[:i+1]
    
    return num

# Using inbuilt function rstrip.

def removeTrailingZeros2(num):
    if num=="0":
        return num
    return num.rstrip("0")

# Testcases
testcases=["109000","1","22","220","0","22220003000320"]
for testcase in testcases:
    print(removeTrailingZeros(testcase))
    print(removeTrailingZeros1(testcase))
    print(removeTrailingZeros2(testcase))
