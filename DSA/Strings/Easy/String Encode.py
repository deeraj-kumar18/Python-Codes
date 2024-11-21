'''
String Encode

Given a string, compress it using the counts of repeated characters. 

For example, the input aaaabbbbbbcccdd should be encoded as 4a6b3c2d, 
where each sequence of repeated characters is replaced by its count followed by the character.

Example 1:
input:aaaabbbbbbcccdd
output:4a6b3c2d

Example 2:
input:aabbcc
output:2a2b2c

Example 3:
input:abcd
output:1a1b1c1d
'''
# Simple Counting Approach 

def string_encode(string):
    ans=""
    count=1
    for i in range(1,len(string)):
        if string[i-1]==string[i]:
            count+=1
        else:
            ans+=f"{count}{string[i-1]}"
            count=1

    ans+=f"{count}{string[-1]}"

    return ans

# Testing
testcases=["aaaabbbbbbcccdd","aabbcc" ,"abcd" ]
for testcase in testcases:
    print(string_encode(testcase))