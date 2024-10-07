'''
Implement Upper Bound https://www.naukri.com/code360/problems/implement-upper-bound_8165383?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries
Easy

Problem statement
You are given a sorted array ‘arr’ containing ‘n’ integers and an integer ‘x’.Implement the ‘upper bound’ function to find the index of the upper bound of 'x' in the array.

Note:
1. The upper bound in a sorted array is the index of the first value that is greater than a given value. 
2. If the greater value does not exist then the answer is 'n', Where 'n' is the size of the array.
3. Try to write a solution that runs in log(n) time complexity.

Example:
Input : ‘arr’ = {2,4,6,7} and ‘x’ = 5,
Output: 2

Explanation: The upper bound of 5 is 6 in the given array, which is at index 2 (0-indexed).

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= ‘n’ <= 10^5
1 <= ‘x’ <= 10^9
1 <= ‘arr[i]’ <= 10^9
Time Limit: 1 sec

Sample Input 1:
5 7
1 4 7 8 10

Sample Output 1:
3   

Explanation of sample output 1:
In the given test case, the lowest value greater than 7 is 8 and is present at index 3(0-indexed). 

Sample Input 2:
5 10
1 2 5 6 10   
Sample Output 2:
5
'''
def upper_bound(arr,n,x):
    low,high=0,n-1
    ans=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            ans=mid
            high=mid-1
            
        else:
            low=mid+1
    
    return ans


# Test cases
test_cases = [
    ([1, 4, 7, 8, 10], 5, 7, 3),      # Test Case 1
    ([1, 2, 5, 6, 10], 5, 10, 5),     # Test Case 2
    ([2, 4, 6, 7], 4, 5, 2),          # Test Case 3
    ([2, 4, 6, 7, 9, 12, 14], 7, 10, 5),  # Test Case 4
    ([5], 1, 3, 0),                   # Test Case 5
    ([5], 1, 5, 1),                   # Test Case 6
    ([1, 2, 4, 4, 6, 9], 6, 4, 4),    # Test Case 7
    ([2, 5, 8, 12, 16], 5, 11, 3),    # Test Case 8
]

for i, (arr, n, x, expected) in enumerate(test_cases, 1):
    result = upper_bound(arr, n, x)
    print(f"Test Case {i}: arr = {arr}, x = {x}")
    print(f"Expected Output: {expected}, Your Output: {result}")
    print(f"Test {'Passed' if result == expected else 'Failed'}\n")