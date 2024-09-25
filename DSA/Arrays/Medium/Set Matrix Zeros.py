'''
73. Set Matrix Zeroes   https://leetcode.com/problems/set-matrix-zeroes/description/
Medium
Hint Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
'''
# BruteForce Approach
'''
Approach: We iterate over the matrix and if we encounter a 0 then we mark the row and col with -1.
why -1? because if we mark it zero directly, then we can end up marking the wrong rows and colums when we encounter a zero in future.
after completely iterating over the array, we iterate over it once again and if we find a -1, then we mark it as 0. we return the matrix.

TC: O(n*m)*O(n+m) == O(N^3)
SC: O(1)
'''
def markRow(matrix, n, m, i):
    # set all non-zero elements as -1 in the row i:
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCol(matrix, n, m, j):
    # set all non-zero elements as -1 in the col j:
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def zeroMatrix(matrix, n, m):
    # Set -1 for rows and cols that contains 0. Don't mark any 0 as -1:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(matrix, n, m, i)
                markCol(matrix, n, m, j)
    
    # Finally, mark all -1 as 0:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    
    return matrix


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
ans=(zeroMatrix(matrix,len(matrix),len(matrix[0])))
for row in ans:
    for ele in row:
        print(ele,end=" ")
    print()

# Better Approach 
'''
Instead of marking the rows and columns while iterating the matrix, instead 
we create two arrays of size n and m resp to mark the rows and cols which have 0 in them.
Even if we have one 0 in a row or col, that row and col elements will be zero.
Later we iterate over the matrix and check if the row or col indices are marked in the arrays, if yes,
then the element will be updated as 0.
TC: O(n*m)
SC: O(n)+O(m)  
'''
def zeroMatrix1(matrix):
    n=len(matrix)
    m=len(matrix[0])

    row=[0]*n   # row array
    col=[0]*m   # col array

    # Traverse the matrix:
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                 # mark ith index of row wih 1:
                row[i] = 1
                # mark jth index of col wih 1:
                col[j] = 1
    
    # Finally, mark all (i, j) as 0
    # if row[i] or col[j] is marked with 1.
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j]=0
    
    return matrix

print()
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
ans=(zeroMatrix1(matrix1))
for row in ans:
    for ele in row:
        print(ele,end=" ")
    print()