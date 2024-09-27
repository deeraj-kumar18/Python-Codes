'''
867. Transpose Matrix       https://leetcode.com/problems/transpose-matrix/description/
Easy 

Hint: Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
'''
# Approach 1
'''
Here we create a new matrix and update the values in it. It will take us O(N) extra space.
TC: O(2 * N^2)
Sc: O(N^2) bcoz we are using a 2D list.
'''
def transpose(matrix):
    n=len(matrix)
    m=len(matrix[0])
    transpose=[[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transpose[j][i]=matrix[i][j]
    
    return transpose


A = [[ [1, 1, 1, 1], 
 [2, 2, 2, 2], 
 [3, 3, 3, 3], 
 [4, 4, 4, 4]] ,

[[1,2],[2,3],[3,4]]]

for mat in A:
    ans=transpose(mat)
    for row in ans:
        print(row)
    print()

# Approach 2 : Swapping Inplace
'''
We swap the elements in place by only traversing limitedly.
TC: O(N^2)
SC: O(1)
'''
def transpose_inplace(matrix):
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n):
        for j in range(i+1,m):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    return matrix

for mat in A:
    ans=transpose_inplace(mat)
    for row in ans:
        print(row)
    print()

# This works only for SQAURE MATRIX.