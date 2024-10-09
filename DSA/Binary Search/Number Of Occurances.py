'''
Number of occurrence  https://shorturl.at/AOiA6
Difficulty: Medium

Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

Example 1:

Input:
N = 7, X = 2
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 4
Explanation: x = 2 occurs 4 times in the given array so the output is 4.
Example 2:

Input:
N = 7, X = 4
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 0
Explanation: X = 4 is not present in the given array so the output is 0.
Your Task:
You don't need to read input or print anything.
Your task is to complete the function count() which takes the array of integers arr, n, and x as parameters and returns an integer denoting the answer.
If x is not present in the array (arr) then return 0.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ 106
1 ≤ X ≤ 106
'''
# Approach
'''
We subtract first index from last index and add 1 to that.
'''

def count(nums, n, target):
    # Searching for First
    low=0
    high=n-1
    first=-1 
    while(low<=high):
        mid=(low+high)//2
        if nums[mid]==target:
            first= mid
            high=mid-1
        elif target>nums[mid]: # If the target element is greater than mid element, we search the RIGHT half
            low=mid+1       
        else:
            high=mid-1  # If the target element is lesser than mid element, we search the LEFT half

    # Searching For Last
    low=0
    high=n-1
    last=-1
    while(low<=high):
        mid=(low+high)//2
        if nums[mid]==target:
            last= mid
            low=mid+1
        elif target>nums[mid]: # If the target element is greater than mid element, we search the RIGHT half
            low=mid+1       
        else:
            high=mid-1  # If the target element is lesser than mid element, we search the LEFT half

    if first==-1:
        return 0
    return last-first+1 


n=7
target=2
nums=[1, 1, 2, 2, 2, 2, 3]
print(count(nums,n,target))