'''
189. Rotate Array   https://leetcode.com/problems/rotate-array/description/
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''

# IDEA: To shift the k elements to a temporary array. And shifting the elements in their position.
#  Place the elements of temp array back to main array.
#  
def rotate_array(nums,k):
    n=len(nums)
    k=k%n   # To manage the k values greater than n.

    temp=[0]*k # Array of size k to store the elements which need to be moved.

    #  Shifting k elements to the temp array.
    for i in range(k):
        temp[i]=nums[n-k+i]  
    
    # Shifting elements to their right position
    i=k
    j=0
    while(i>=0):
        nums[k+i]=nums[k-j]
        j+=1
        i-=1
    
    # Inserting elements of temp array to nums
    for i in range(k):
        nums[i]=temp[i]
    
    return nums
