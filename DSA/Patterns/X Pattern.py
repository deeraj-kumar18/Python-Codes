'''
Problem: Generate an X Shape Pattern with Numbers

Write a program that takes an integer input n and prints an X shape pattern using numbers. The
numbers decrease as they move towards the center of the X, and then increase as they move away
from the center.

Input Format:
- A single integer n where 1 <= n <= 100.

Output Format:
- The X shape pattern of numbers as described.

Example:
Input:
5

Output:
5       5 
  4   4   
    3     
  2   2   
1       1 
'''
def x_pattern(n):
    c=n
    for i in range(n):
        for j in range(n):
            if i==j or i+j==n-1:
                print(c,end=" ")
            else:
                print(" ",end=" ")
        print()
        
        c=c-1


x_pattern(int(input()))

