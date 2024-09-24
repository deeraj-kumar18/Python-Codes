'''
Array Leaders   https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=leaders-in-an-array
Difficulty: Easy

Given an array arr of n positive integers, your task is to find all the leaders in the array. An element of the array is considered a leader if it is greater than all the elements on its right side or if it is equal to the maximum element on its right side. The rightmost element is always a leader.

Examples
Input: n = 6, arr[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
Input: n = 5, arr[] = {10,4,2,4,1}
Output: 10 4 4 1
Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right. side
Input: n = 4, arr[] = {5, 10, 20, 40} 
Output: 40
Explanation: When an array is sorted in increasing order, only the rightmost element is leader.
Input: n = 4, arr[] = {30, 10, 10, 5} 
Output: 30 10 10 5
Explanation: When an array is sorted in non-increasing order, all elements are leaders.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 <= n <= 107
0 <= arr[i] <= 107
'''
# BruteForce Approach 
'''
Using two forloops, iterate over the list to find if any element is larger than the current index.
TC: O(N^2)
SC: O(N) (Worst Case : When array is sorted in reverse fashion.)
'''
def leaders(arr):
    ans=[]
    for i in range(len(arr)):
        leader=True
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                leader=False
                break
        if leader:
            ans.append(arr[i])
    
    return ans

testcases= [[16,17,4,3,5,2],[10,4,2,4,1],[5, 10, 20, 40],[30, 10, 10, 5]]
for test in testcases:
    print(leaders(test))

# Optimal Approach 
'''
Iterate the array from behind and append the maximum number to ans list by comparing it with the current element.
TC: O(N)
SC: O(N)
'''
def leaders1(arr):
    maxi=float('-inf')
    ans=[]
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>=maxi:
            ans.append(arr[i])
        maxi=max(maxi,arr[i])
    
    return (ans[::-1])

print()
for test in testcases:
    print(leaders1(test))