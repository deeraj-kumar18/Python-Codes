'''
Odd or Even         https://www.geeksforgeeks.org/problems/odd-or-even3618/1

Difficulty: Basic

Given a positive integer n, determine whether it is odd or even. Return a string "even" if the number is even and "odd" if the number is odd.

Examples:
Input: n = 15
Output: odd
Explanation: The number is not divisible by 2

Input: n = 44
Output: even
Explanation: The number is divisible by 2

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
0 <= n <= 10^4
'''

def oddEven(n):
    if n & 1 !=0:
        return "Odd"
    else:
        return "Even"

for i in range(50):
    print(f"The number {i} is:",oddEven(i))    