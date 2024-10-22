'''
Problem: Print a Butterfly Pattern of Stars

Write a program that takes an integer input n and prints a butterfly pattern using stars ('*'). The
butterfly pattern should have 2n rows. The first n rows will display stars in increasing order, and the
next n rows will display stars in decreasing order.

For example, if n = 4, the pattern would look like:

*      *
**    **
***  ***
********
********
***  ***
**    **
*      *

Input Format:
- A single integer n where 1 <= n <= 100.

Output Format:
- The butterfly pattern with stars as described.

Example:
Input:
4

Output:
*      *
**    **
***  ***
********
********
***  ***
**    **
*      *
'''
def butterfly(n):
    spaces=(n*2)-2
    for i in range(1,n+1):
        print("*"*i + " "*(spaces) + "*"*i)
        spaces-=2
    
    spaces=0
    for i in range(n,-1,-1):
        print("*"*i + " "*(spaces) + "*"*i)
        spaces+=2


n=10
for i in range(n):
    butterfly(i)