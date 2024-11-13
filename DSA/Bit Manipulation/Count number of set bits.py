'''
Count total set bits        https://www.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1

Difficulty: Medium

You are given a number n. Find the total count of set bits for all numbers from 1 to n (both inclusive).

Examples :

Input: n = 4
Output: 5
Explanation: For numbers from 1 to 4. For 1: 0 0 1 = 1 set bits For 2: 0 1 0 = 1 set bits For 3: 0 1 1 = 2 set bits For 4: 1 0 0 = 1 set bits Therefore, the total set bits is 5.

Input: n = 17
Output: 35
Explanation: From numbers 1 to 17(both inclusive), the total number of set bits is 35.

Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 10^8
'''
# Approach using Modulo and Division.

def countSetBits(n):
        c=0
        while n>1:
            if n%2==1:
                c+=1
            n=n//2
        
        if n==1:
            c+=1
       
        
        return c
    
    
print(countSetBits(15))

# Approach using Right Shift  and bitwise AND.
def countSetBits1(n):
        c=0
        while n>1:
            if n&1==1:
                c+=1
            n=n>>2
        
        if n==1:
            c+=1
       
        
        return c
print(countSetBits(15))