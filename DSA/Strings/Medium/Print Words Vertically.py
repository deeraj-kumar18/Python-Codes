'''
1324. Print Words Vertically        https://leetcode.com/problems/print-words-vertically/description/
Medium

Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

Example 1:
Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"

Example 2:
Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"

Example 3:
Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]
 
Constraints:
1 <= s.length <= 200
s contains only upper case English letters.
It's guaranteed that there is only one space between 2 words.
'''
def print_vertically(s):
    # Splitting the words into a list.
    words=s.split(" ")
    # Finding the maximum length of the words present in the list. 
    max_len=max(len(word) for word in words)
    # Empty list to store the output of strings.
    ans=[]
    # Iterating over the length of maximum word.
    for i in range(max_len):
        # String to store the chars in vertical order
        ele=""
        # Iterating over each word in the list.
        for word in words:
            # If the index is less than the current word length, then we append the char to the string.  
            if i<len(word):
                ele+=word[i]
            # Else we append a space.
            else:
                ele+=" "
        # Appending the string to our list after removing trailing spaces on the right side.
        ans.append(ele.rstrip())
    return ans

s = "CONTEST IS COMING"
print(print_vertically(s))