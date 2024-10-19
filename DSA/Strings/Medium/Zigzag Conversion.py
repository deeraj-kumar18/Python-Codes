'''
6. Zigzag Conversion        https://leetcode.com/problems/zigzag-conversion/description/

Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
 
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
 
Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''
# Approach
"""
if numRows is equal to 1, we return the same string.
we keep two pointers for direction and row_indicator. We flip the direction variable based on the direction of appending as per zigzag condition.
We append the characters one by one in the rows based on the direction.
"""
def convert(s,numRows):
    
    # if numRows is equal to 1, we return the same string.
    if numRows==1 or numRows>len(s):
        return s
    
    direction=1  # Used to indicate the direction. 1 for Downward traversal. -1 for Upward traversal.
    row_indicator=0 # Indicator to append in which row.

    rows=[[] for _ in range(numRows)] # 2D List to store the answer.

    for char in s:
        rows[row_indicator].append(char)  

        if row_indicator==0: # If we come to first row, we change the direction to 1
            direction=1
        elif row_indicator == numRows-1: # If we come to the last row, we change the direction to -1
            direction=-1
        
        row_indicator+=direction # we update the row until the first or last row is encountered.
    
    # Parsing the 2D list into string format.
    ans=""
    for row in rows:
        ans+="".join(row)
    
    return ans

s = "PAYPALISHIRING" 
numRows = 4
print(convert(s,numRows))
