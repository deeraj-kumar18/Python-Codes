'''
Min and Max in Array
Difficulty: Basic 
Given an array arr. Your task is to find the minimum and maximum elements in the array.

Note: Return an array that contains two elements the first one will be a minimum element and the second will be a maximum of an array.

Examples:
Input: arr = [3, 2, 1, 56, 10000, 167]
Output: 1 10000
Explanation: minimum and maximum elements of array are 1 and 10000.
Input: arr = [1, 345, 234, 21, 56789]
Output: 1 56789
Explanation: minimum and maximum element of array are 1 and 56789.
Input: arr = [56789]
Output: 56789 56789
Explanation: Since the array contains only one element so both min & max are same.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <=1012
'''
# TC: O(N) , SC: O(1)

def get_min_max(arr):
    mini=arr[0]
    maxi=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>=maxi:
            maxi=arr[i]
        if arr[i]<=mini:
            mini=arr[i]
    
    return [mini,maxi]

testcases= [[1, 345, 234, 21, 56789],[3, 2, 1, 56, 10000, 167],[56789]]
for testcase in testcases:
    print(get_min_max(testcase))