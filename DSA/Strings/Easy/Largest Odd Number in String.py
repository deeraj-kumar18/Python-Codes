'''
1903. Largest Odd Number in String      https://leetcode.com/problems/largest-odd-number-in-string/description/

Easy

You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

Example 2:
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".

Example 3:
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.

Constraints:
1 <= num.length <= 105
num only consists of digits and does not contain any leading zeros.
'''
# Approach 1
def largestOddNumber(num):
    if int(num)%2==1:
        return num 
    else:
        # Iterating from behind and searching for odd number, if true. we return the slice till that index.
        for i in range(len(num)-2,-1,-1):
            if int(num[i])%2==1:
                return num[:i+1]
    
    # After complete iteration, if there are no odd numbers, then we return an empty string.
    return ""

num="2345356"
print(largestOddNumber(num))

# Approach 2 using Lists
def largestOddNumber1(num):
    n=len(num)
    a=list(num)
    for i in range(n-1,-1,-1):
        if(int(a[i])%2==1):
            return (str("".join(a[:i+1])))
    
    return ""

print(largestOddNumber1(num))

# Approach 3 Using String Method 
def largestOddNumber2(num):
    return num.rstrip('02468')

print(largestOddNumber2(num))