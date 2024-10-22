'''Problem: Create a Checkerboard Pattern in a 2D Matrix            AUTOLAB

You are given two integers `n` and `m` representing the dimensions of a 2D matrix. Your task is to
create a checkerboard pattern in the matrix, where each cell alternates between 0 and 1.

Write a function `create_checkerboard(n, m)` that returns a 2D matrix with a checkerboard pattern of
dimensions `n` x `m`.

Input Format:
- Two integers `n` and `m` (1 <= n, m <= 100), representing the number of rows and columns in the
matrix.

Output Format:
- A 2D list representing the checkerboard pattern of the matrix.

Example:

Input:
n = 3
m = 3

Output:
[
[0, 1, 0],
[1, 0, 1],

[0, 1, 0]
]

Explanation:
The 3x3 matrix follows a checkerboard pattern where every cell alternates between 0 and 1.
'''
import time
# Own Approach
def checkerboard(n,m):
    output=[]
    for i in range(n):
        innerlist=[]
        if i%2==0:
            flag=True
            for j in range(m):
                if flag:
                    innerlist.append(0)
                    flag=False
                else:
                    innerlist.append(1)
                    flag=True
        
        else:
            flag=True
            for j in range(m):
                if flag:
                    innerlist.append(1)
                    flag=False
                else:
                    innerlist.append(0)
                    flag=True

        
        output.append(innerlist)
        
    return output

# Simple Approach
def checkerboard1(n,m):
    output=[]
    for i in range(n):
        innerlist=[]
        for j in range(m):
            innerlist.append((i+j)%2) # sum of the indices will result in either 0 or 1. so we append accordingly.
        output.append(innerlist)

    return output

n=int(input())
m=int(input())
print(checkerboard(n,m))
print(checkerboard1(n,m))
