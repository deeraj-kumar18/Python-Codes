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
def convert(s,numRows):
    if numRows==1 or numRows>len(s):
        return s
    
    direction=1
    row_indicator=0

    rows=[[] for _ in range(numRows)]

    for char in s:
        rows[row_indicator].append(char)

        if row_indicator==0:
            direction=1
        elif row_indicator == numRows-1:
            direction=-1
        
        row_indicator+=direction
    
    ans=""
    for row in rows:
        ans+="".join(row)
    
    return ans

s = "PAYPALISHIRING" 
numRows = 4
print(convert(s,numRows))
