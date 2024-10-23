'''
Problem: Generate a Rhombus Pattern with Characters         AUTOLAB

Write a program that takes an integer input n and prints a rhombus pattern using letters from the
alphabet (A-Z). The rhombus should have n rows on both the top and bottom half. The center of the
rhombus will contain the letter corresponding to the nth position in the alphabet.

Input Format:
- A single integer n where 1 <= n <= 26.

Output Format:
- The rhombus pattern with letters as described.

Example:
Input:
4

Output:
      A 
    B B 
  C C C 
D D D D 
  C C C 
    B B 
      A 
'''
def rhombus_pattern(n):
    var=65
    for i in range(n):
        print(" "*(n-i-1)*2 + (chr(var+i) + " ")*(i+1))

    
    for i in range(n-2,-1,-1):
        print(" "*(n-i-1)*2 + (chr(var+i) + " ")*(i+1))
    
    return

rhombus_pattern(int(input()))