'''
Bit Manipulation            https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bit-manipulation

Difficulty: Easy

Given a 32 bit unsigned integer num and an integer i. Perform following operations on the number - 

1. Get ith bit

2. Set ith bit

3. Clear ith bit

Note : For better understanding, we are starting bits from 1 instead 0. (1-based). You have to print space three space seperated values ( as shown in output without a line break) and do not have to return anything.

Examples :
Input: 70 3
Output: 1 70 66
Explanation: Bit at the 3rd position from LSB is 1. (1 0 0 0 1 1 0) .The value of the given number after setting the 3rd bit is 70. The value of the given number after clearing 3rd bit is 66. (1 0 0 0 0 1 0)

Input: 8 1
Output: 0 9 8
Explanation: Bit at the first position from LSB is 0. (1 0 0 0)  .The value of the given number after setting the 1st bit is 9. (1 0 0 1).  The value of the given number after clearing 1st bit is 8. (1 0 0 0)
 

Constraints:
0<=num<=10^9
1<=i<=32
'''
def bitManipulation(num, i):
        # Code here
    ans=""

    # Getting ith bit
    a=num>>i-1
    if a&1==1:
        ans+="1"
        ans+=" "
    else:
        ans+="0"
        ans+=" "

    # # Setting ith bit
    b=num | ( 1<<i-1)
    ans+=str(b)
    ans+=" "
    
    # # Clearing ith bit.
    c=~(1<<i-1) & num
    ans+=str(c)
    ans+=" "
    
    print(ans.strip())

bitManipulation(70,3)
bitManipulation(8,1)