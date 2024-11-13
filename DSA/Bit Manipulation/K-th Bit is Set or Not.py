'''
K-th Bit is Set or Not          https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1
Difficulty: Easy

Given a number n and a bit number k, check if the kth index bit of n is set or not. A bit is called set if it is 1. The position of set bit '1' should be indexed starting with 0 from the LSB side in the binary representation of the number.
Note: Index is starting from 0. You just need to return true or false, driver code will take care of printing "Yes" and "No".

Examples : 
Input: n = 4, k = 0
Output: false
Explanation: Binary representation of 4 is 100, in which 0th index bit from LSB is not set. So, return false.

Input: n = 4, k = 2
Output: true
Explanation: Binary representation of 4 is 100, in which 2nd index bit from LSB is set. So, return true.

Input: n = 500, k = 3
Output: false
Explanation: Binary representation of 500 is 111110100, in which 3rd index bit from LSB is not set. So, return false.

Constraints:
1 ≤ n ≤ 10**9
0 ≤ k ≤ 31
'''
# Using Right Shift.
def check_if_set(n,k):
    # we are right-shifting the number k times to get the digit at ones place. 
    num=n>>k
    # We perform bitwise AND operation between num and 1, if the ones digit is 1 , then the output will be 1 else 0 
    if num & 1 != 0:
        return True
    else:
        return False

print(check_if_set(4,0))

# Using Left Shift.
def check_if_set1(n,k):
    # We left shift 1 by k times to generate the number which is equivalent to the set bit.
    num=1<<k
    if num & n != 0:
        return True
    else:
        return False

print(check_if_set1(4,0))