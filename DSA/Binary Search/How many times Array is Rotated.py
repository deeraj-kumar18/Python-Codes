'''
Find Kth Rotation       https://www.geeksforgeeks.org/problems/rotation4723/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=rotation
Difficulty: Easy

Given an increasing sorted rotated array arr of distinct integers. The array is right-rotated k times. Find the value of k.
Let's suppose we have an array arr = [2, 4, 6, 9], so if we rotate it by 2 times so that it will look like this:
After 1st Rotation : [9, 2, 4, 6]
After 2nd Rotation : [6, 9, 2, 4]

Examples:
Input: arr = [5, 1, 2, 3, 4]
Output: 1
Explanation: The given array is 5 1 2 3 4. The original sorted array is 1 2 3 4 5. We can see that the array was rotated 1 times to the right.

Input: arr = [1, 2, 3, 4, 5]
Output: 0
Explanation: The given array is not rotated.

Expected Time Complexity: O(log(n))
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <=105
1 <= arri <= 107
'''
# Optimal Approach 
'''
Observation: The number of times an array is rotated is equal to the index of the minimum value.
'''

def findKRotation(nums):
    low,high=0,len(nums)-1
    ans=float('inf')
    index1=-1

    while low<=high:
        mid=(low+high)//2
        # Left half sorted
        if nums[low]<=nums[mid]:
            if nums[low]<ans:
                index1=low
                ans=nums[low]
            low=mid+1
        # Right half sorted
        else:
            if nums[mid]<ans:
                index1=mid
                ans=nums[mid]   # Mid is the least element if the right half is sorted.
            high=mid-1

    return index1

arr = [6,1, 2, 3, 4, 5]
print(findKRotation(arr))