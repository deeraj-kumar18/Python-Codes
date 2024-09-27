'''
54. Spiral Matrix       https://leetcode.com/problems/spiral-matrix/description/
Medium
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''
# Approach
'''
We keep 4 pointers and iterate using loops between the pointers in a order. 
left -> right
top -> bottom
right -> left
bottom -> top
We increment and decrement the pointers based on the requirement. 
'''
def spiralOrder(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    left,right=0,cols-1
    top,bottom=0,rows-1
    # print(left,right,top,bottom)

    ans=[]
    while(top<=bottom and left<=right):

        for i in range(left,right+1):
            ans.append(matrix[top][i])
        top+=1

        for i in range(top,bottom+1):
            ans.append(matrix[i][right])
        right-=1

        if(top<=bottom):
            for i in range(right,left-1,-1):
                ans.append(matrix[bottom][i])
            bottom-=1

        if(left<=right):
            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])
            left+=1

    return ans

testcases = [[[1,2,3],
              [4,5,6],
              [7,8,9]],

             [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]],

             [[1,2,3],
              [8,9,4],
              [7,6,5]]]

for testcase in testcases:
    print(spiralOrder(testcase))