'''
Floor in a Sorted Array / Lower Bound in a Sorted Array         https://www.naukri.com/code360/problems/lower-bound_8165382?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries
Implement Lower Bound
Easy

Problem statement
You are given an array 'arr' sorted in non-decreasing order and a number 'x'. You must return the index of the lower bound of 'x'.

Note:
1. For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such that the value 'arr[idx]' is not less than 'x'.If all numbers are smaller than 'x', then 'n' should be the 'lower_bound' of 'x', where 'n' is the size of array.

2. Try to do this in O(log(n)).

Example:
Input: ‘arr’ = [1, 2, 2, 3] and 'x' = 0

Output: 0

Explanation: Index '0' is the smallest index such that 'arr[0]' is not less than 'x'.


Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= ‘n’ <= 10^5
0 <= ‘arr[i]’ <= 10^5
1 <= ‘x’ <= 10^5
Sample Input 1:
6
1 2 2 3 3 5
0


Sample Output 1:
0


Explanation Of Sample Input 1 :
Index '0' is the smallest index such that 'arr[0]' is not less than 'x'.
Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ n ≤ 107
1 ≤ arr[i] ≤ 1018
0 ≤ x ≤ arr[n-1] 
'''
def lowerBound(arr,n,target):
    low,high=0,n-1
    ans=n

    while low<=high:
        mid=(low+high)//2

        #case 1: If the mid element is greater than target, that can be our ans. and we can find better ans in the left half.
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else: # if the mid element is smaller than target, then we eliminate the left half and search in right half.
            low=mid+1
    return ans


# Test cases
test_cases = [
    ([3, 5, 8, 15, 19], 5, 9, 3),  # Test Case 1
    ([3, 5, 8, 15, 19], 5, 5, 1),  # Test Case 2
    ([3, 5, 8, 15, 19], 5, 20, 5), # Test Case 3
    ([3, 5, 8, 15, 19], 5, 2, 0),  # Test Case 4
    ([1, 4, 6, 7, 9], 5, 6, 2),    # Test Case 5
    ([10], 1, 9, 0),               # Test Case 6
    ([10], 1, 11, 1),              # Test Case 7
]

for i, (arr, n, x, expected) in enumerate(test_cases, 1):
    result = lowerBound(arr, n, x)
    print(f"Test Case {i}: arr = {arr}, x = {x}")
    print(f"Expected Output: {expected}, Your Output: {result}")
    print(f"Test {'Passed' if result == expected else 'Failed'}\n")