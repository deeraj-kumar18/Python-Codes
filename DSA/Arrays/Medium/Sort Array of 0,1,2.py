'''
75. Sort Colors  https://leetcode.com/problems/sort-colors/description/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
 
Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
'''
# Brute Force Solution
'''
Sort using any sorting technique. Preferably with less time complexity.
ex. Merge Sort O(n log n) , O(n)'''
def sort_bruteforce(arr):
    # Using Bubble Sort
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)

a=[0,1,0,2,0,1,0,2,0,1,0,2,0,1,0,2,0,1,0,1,0,1,0,2,0]
sort_bruteforce(a)

# Better Solution 
'''
The intuition is simple, we iterate over the array and count the number of 0,1,2s. 
then iterate over the counts of individual numbers and overwrite the values in the list with 
respective 0,1,2.
Time Complexity: O(2N) Space Complexity: O(1)
'''
def sort_better(arr):
    count0,count1,count2=0,0,0
    for i in arr:
        if i == 0:
            count0+=1
        elif i == 1:
            count1+=1
        else:
            count2+=1
    
    for i in range(count0):
        arr[i]=0
    
    for i in range(count1):
        arr[i+count0]=1
    
    for i in range(count2):
        arr[i+count0+count1]=2
    
    print(arr)

sort_better(a)

# Optimal Approach
'''
Dutch National Flag Approach
This algorithm contains 3 pointers i.e. low, mid, and high, and 3 main rules.  The rules are the following:
arr[0….low-1] contains 0. [Extreme left part]
arr[low….mid-1] contains 1.
arr[high+1….n-1] contains 2. [Extreme right part], n = size of the array
'''
def sort_optimal(arr):
    low,mid,high=0,0,len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        
        elif arr[mid]==1:
            mid+=1
        
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    print(arr)

sort_optimal(a)