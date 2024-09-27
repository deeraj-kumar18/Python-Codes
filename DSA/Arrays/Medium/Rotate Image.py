'''
48. Rotate Image            https://leetcode.com/problems/rotate-image/description/
Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
'''
# Brute force Approach  (Own)
def rotate(matrix):
    n=len(matrix) #rows 
    m=len(matrix[0]) # columns 
    b=[[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            b[j][i]=matrix[i][j]
    
    
    res=[]
    for row in b:
        res.append(row[::-1])
    
    for i in range(n):
        for j in range(m):
            matrix[i][j]=res[i][j]
    
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))
# Brute Force Approach Strivers
'''
Observe the pattern in indices. 
[i][j] goes to [j][n-1-i]
TC: O(N^2)
SC: O(N^2)
'''
def rotate1(matrix):
    n=len(matrix) #rows 
    # m=len(matrix[0]) # columns 
    b=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            b[j][n-1-i]=matrix[i][j]
    
    return b
print()
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate1(matrix1))