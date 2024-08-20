'''
Python – Replace all occurrences of a substring in a string

Sometimes, we need to replace all occurrences of a substring with other.

Input : test_str = “geeksforgeeks” s1 = “geeks” s2 = “abcd” 
Output : test_str = “abcdforabcd” Explanation : We replace all occurrences of s1 with s2 in test_str. 

Input : test_str = “geeksforgeeks” s1 = “for” s2 = “abcd” 
Output : test_str = “geeksabcdgeeks”
'''
# USING INBUILT FUNCTIONS.
def replace(test_Str,s1,s2):
    return test_Str.replace(s1,s2)

test_str = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"
print(replace(test_str,s1,s2))