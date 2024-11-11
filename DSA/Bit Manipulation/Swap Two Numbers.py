'''
Swap two numbers

Difficulty: Basic

Swap given two numbers and print them. (Try to do it without a temporary variable.) and return it.

Example 1:
Input: a = 13, b = 9
Output: 9 13
Explanation: after swapping it
becomes 9 and 13.

Example 2:
Input: a = 15, b = 8
Output: 8 15
Explanation: after swapping it
becomes 8 and 15.

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ a, b ≤ 10**6
'''
# Approach using XOR Operation
'''
In XOR operation, 
if the inputs are same, the output is 0
else, output is 1.

Here , we perform XOR operation thrice to swap the numbers.
'''
def swap(a,b):
    print("Before Swapping:",a,b)
    a=a^b  
    b=a^b
    a=a^b
    print("After Swapping:",a,b)

swap(2,3)

# Method 1 (Using Arithmetic Operators) 
def swap1(x,y):
    print("Before Swapping:",x,y)
    x = x + y

    y = x - y

    x = x - y
    print("After Swapping:",x,y)

swap1(2,3)
