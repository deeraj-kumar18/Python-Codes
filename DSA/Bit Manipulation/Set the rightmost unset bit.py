'''
Set the rightmost unset bit         https://www.geeksforgeeks.org/problems/set-the-rightmost-unset-bit4436/1
Difficulty: Basic

Given a non-negative number n . The problem is to set the rightmost unset bit in the binary representation of n.

Examples :
Input: n = 6
Output: 7
Explanation: The binary representation of 6 is 110. After setting right most bit it becomes 111 which is 7.

Input: n = 15
Output: 31
Explanation: The binary representation of 15 is 01111. After setting right most bit it becomes 11111 which is 31.

Expected Time Complexity: O(Logn)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 10**9
'''
def set_rightmost(n):
    next_num=n+1    # Adding 1 to n effectively flips all the trailing 1s in n to 0 and the first 0 to 1.
    # When we perform an OR operation with the original number, it sets the rightmost 0 bit in n to 1, without affecting any other bits.
    return n | next_num

print(set_rightmost(15))