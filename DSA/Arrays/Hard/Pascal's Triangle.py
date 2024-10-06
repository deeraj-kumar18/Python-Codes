'''
118. Pascal's Triangle      https://leetcode.com/problems/pascals-triangle/description/
Easy
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
'''
def pascal_triangle(n):
    a=[[1]]
    for i in range(n-1):
        b=[1]
        for j in range(len(a[i])-1):
            b.append(a[i][j]+a[i][j+1])

        b.append(1)  # for every sublist the last element is 1
        a.append(b)
        
    return a


for i in range(1,6):
    print(f"Pascal Triangle of {i} number of rows:")
    print(pascal_triangle(i))
    print()

# Variation using NcR formula. 

from typing import *

def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return int(res)

def pascalTriangle(n : int) -> List[List[int]]:
    ans = []

    #Store the entire pascal's triangle:
    for row in range(1, n+1):
        tempLst = [] # temporary list
        for col in range(1, row+1):
            tempLst.append(nCr(row - 1, col - 1))
        ans.append(tempLst)
    return ans

if __name__ == '__main__':
    n = 5
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()
