'''
Peak element   https://www.geeksforgeeks.org/problems/peak-element/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
Difficulty: Basic 
Given an 0-indexed array of integers arr[] of size n, find its peak element and return it's index. An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist).

Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.

Examples :

Input: n = 3, arr[] = {1, 2, 3} 
Output: 1
Explanation: If the index returned is 2, then the output printed will be 1. Since arr[2] = 3 is greater than its adjacent elements, and there is no element after it, we can consider it as a peak element. No other index satisfies the same property, so answer will be printed as 0.
Input: n = 7, arr[] = {1, 1, 1, 2, 1, 1, 1}
Output: 1
Explanation: In this case there are 5 peak elements with indices as {0,1,3,5,6}. Returning any of them will give you correct answer.
Your Task:
You don't have to read input or print anything. Complete the function peakElement() which takes the array arr[] and its size n as input parameters and returns the index of the peak element.

Expected Time Complexity: O( log(n) ).
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 106
'''

# Time complexity: O(n), One traversal is needed so the time complexity is O(n)
# Auxiliary Space: O(1), No extra space is needed, so space complexity is constant

def peakelement(arr,n):
    # Edge Cases
    # 1. if the length of the list is 1, then we return index 0.
    if n==1:
        return 0
    # 2. If the first element is greater than the second element, then we can consider it as Peak element
    #    and return 0.
    if arr[0]>arr[1]:
        return 0
    # 3. If the last element is greater than the second last element,then its a peak element.
        # so we can return n-1 index(last element).
    if arr[n-1]>=arr[n-2]:
        return n-1
    #  For finding peak element in the middle of the array.
    for i in range(1,n-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            return i

# Driver code
def test_peakelement():
    test_cases = [
        # Test case 1: Peak is at the last element
        ([1, 2, 3], 3, [2]),
        
        # Test case 2: Multiple peaks, any valid peak can be returned
        ([1, 1, 1, 2, 1, 1, 1], 7, [0, 1, 3, 5, 6]), 
        
        # Test case 3: Single element, peak is at index 0
        ([10], 1, [0]),
        
        # Test case 4: Peak at the first element
        ([5, 3, 4, 2, 1], 5, [0]),
        
        # Test case 5: Peak in the middle
        ([1, 3, 20, 4, 1, 0], 6, [2]),
    ]
    
    for i, (arr, n, expected) in enumerate(test_cases):
        result = peakelement(arr, n)
        if result in expected:
            print(f"Test case {i+1} passed: Peak found at index {result}")
        else:
            print(f"Test case {i+1} failed: Expected one of {expected}, but got {result}")

# Run the test cases
test_peakelement()