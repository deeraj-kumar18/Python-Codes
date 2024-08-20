'''
Python – Replace all occurrences of a substring in a string

Sometimes, we need to replace all occurrences of a substring with other.

Input : test_str = “geeksforgeeks” s1 = “geeks” s2 = “abcd” 
Output : test_str = “abcdforabcd” Explanation : We replace all occurrences of s1 with s2 in test_str. 

Input : test_str = “geeksforgeeks” s1 = “for” s2 = “abcd” 
Output : test_str = “geeksabcdgeeks”
'''
# USING INBUILT FUNCTION REPLACE.
def replace(test_Str,s1,s2):
    return test_Str.replace(s1,s2)

test_str = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"
print(replace(test_str,s1,s2))

# USING SPLIT.
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