'''
Python – Replace all occurrences of a substring in a string

Sometimes, we need to replace all occurrences of a substring with other.

Input : test_str = “geeksforgeeks” s1 = “geeks” s2 = “abcd” 
Output : test_str = “abcdforabcd” Explanation : We replace all occurrences of s1 with s2 in test_str. 

Input : test_str = “geeksforgeeks” s1 = “for” s2 = “abcd” 
Output : test_str = “geeksabcdgeeks”
'''
# USING INBUILT FUNCTION REPLACE.  
'''
Time Complexity: O(n)
Auxiliary Space: O(n)
'''
def replace(test_Str,s1,s2):
    return test_Str.replace(s1,s2)

test_str = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"
print(replace(test_str,s1,s2))

# USING SPLIT.
'''
Time Complexity: O(n)
Auxiliary Space: O(n)
'''
def replace1(test_str,s1,s2):
    s=test_str.split(s1)  # splitting the given sentence on the basis of target word.
    # print(s)  # debug statement.
    output=""
    for i in s:
        if i=="":
            output+=s2
        else:
            output+=i

    return output

test_str = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"
print(replace1(test_str,s1,s2))

# USING ITERATION
'''
Time complexity: O(nm), where n is the length of the input string and m is the length of the substring to be replaced. 
Auxiliary space: O(n), since we are creating a new string to store the result.
'''
def replace_substring(test_str,s1,s2):
    result=""
    i=0
    while i<len(test_str):
        if test_str[i:i+len(s1)] == s1:
            result+=s2
            i+=len(s1)
        else:
            result+=test_str[i]
            i+=1
    return result

test_str = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"
print(replace_substring(test_str,s1,s2))