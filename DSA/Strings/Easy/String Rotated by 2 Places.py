'''
String Rotated by 2 Places
Difficulty: Easy

Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating (in any direction) string 'a' by exactly 2 places.

Example 1:
Input:
a = amazon
b = azonam
Output: 
1
Explanation: 
amazon can be rotated anti-clockwise by two places, which will make it as azonam.

Example 2:
Input:
a = geeksforgeeks
b = geeksgeeksfor
Output: 
0
Explanation: 
If we rotate geeksforgeeks by two place in any direction, we won't get geeksgeeksfor.

Expected Time Complexity: O(N).
Expected Auxilary Complexity: O(N).
Challenge: Try doing it in O(1) space complexity.

Constraints:
1 ≤ length of a, b ≤ 105
'''
def isRotated(str1,str2):

    if len(str1)!=len(str2):
        return False
        
    # right rotation
    rr=str1[-2:]+str1[:-2]
    
    # left rotation
    lr=str1[2:]+str1[:2]
    
    if rr==str2 or lr==str2:
        return True
    
    return False

a = 'geeksforgeeks'
b = 'geeksgeeksfor'
print(isRotated(a,b))